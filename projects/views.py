from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone

from fehler_auth.models import User

from .serializers import ProjectSerializer, TaskSerializer, RiskSerializer
from .models import Project, ProjectMembership, Task, Risk
from spaces.models import Space


class ListProjects(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, space_name):
        """
        Return a list of all projects a particular user is associated with.
        """
        project_memberships = ProjectMembership.objects.filter(user=request.user.id)
        # only return projects from that particular space.
        user_projects = [
            {
                "id": project_membership.project_id,
                "name": project_membership.project.name,
                "space": project_membership.project.space.name,
            }
            for project_membership in project_memberships
            if project_membership.project.space.name == space_name
        ]
        return Response(user_projects, status=status.HTTP_200_OK)


class AddProjectMember(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, space_name, project_name):
        """
        Add a user to a project.
        """
        space = Space.objects.get(name=space_name)
        user = User.objects.get(email=request.data["email"])
        if user in space.get_members():
            project = Project.objects.get(name=project_name, space__name=space_name)

            project_membership = ProjectMembership(
                project=project, user=user, date_joined=timezone.now()
            )
            project_membership.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateProject(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a new project with provided credentials.
        """
        project_serializer = ProjectSerializer(data=request.data)
        if project_serializer.is_valid(raise_exception=True):
            new_project = project_serializer.save()
            if new_project:
                owner_email = request.data["owner"]
                owner = User.objects.get(email=owner_email)
                user = self.create_project_membership(owner, new_project.id)
                project_memberships = ProjectMembership.objects.filter(user=owner)
                user_projects = [
                    {
                        "id": project_membership.project_id,
                        "name": project_membership.project.name,
                        "space": project_membership.project.space.name,
                    }
                    for project_membership in project_memberships
                ]
                return Response(user_projects, status=status.HTTP_200_OK)
        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_project_membership(self, user, project_id):
        project = Project.objects.get(id=project_id)
        user = ProjectMembership.objects.create(user=user, project=project)
        user.save()


class DeleteProject(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, project_id):
        """
        Delete a project with provided credentials.
        """
        project = Project.objects.get(id=project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateProject(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, project_id):
        """
        Update a project with provided credentials.
        """
        project = Project.objects.get(id=project_id)
        project_serializer = ProjectSerializer(project, data=request.data)
        if project_serializer.is_valid(raise_exception=True):
            project_serializer.save()
            return Response(project_serializer.data, status=status.HTTP_200_OK)
        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListTasks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return a list of all tasks associated with a particular project.
        """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        project_tasks = [
            {
                "id": task.id,
                "name": task.name,
                "project": task.project.name,
                "type": task.type,
                "description": task.description,
                "assignee": task.assignee.email if task.assignee else None,
                "labels": task.labels,
                "reporter": task.reporter.email if task.reporter else None,
                "status": task.status,
            }
            for task in tasks
        ]
        return Response(project_tasks, status=status.HTTP_200_OK)


class CreateTask(APIView):
    def post(self, request):
        """
        Create a new task with provided credentials.
        """
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid(raise_exception=True):
            new_task = task_serializer.save()
            # task_serializer.save()

            if new_task:
                tasks = Task.objects.all()

                project_tasks = [
                    {
                        "id": task.id,
                        "name": task.name,
                        "project": task.project.name,
                        "type": task.type,
                        "description": task.description,
                        "assignee": task.assignee.email if task.assignee else None,
                        "labels": task.labels,
                        "reporter": task.reporter.email if task.reporter else None,
                        "status": task.status,
                    }
                    for task in tasks
                ]
            return Response(project_tasks, status=status.HTTP_200_OK)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTask(APIView):
    def delete(self, request, task_id):
        """
        Delete a task with provided credentials.
        """
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateTask(APIView):
    def put(self, request, task_id, format=None):
        """
        Update a task with provided credentials.
        """
        task = Task.objects.get(id=task_id)
        task_serializer = TaskSerializer(task, data=request.data)
        if task_serializer.is_valid(raise_exception=True):
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_200_OK)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignTask(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id, space_name, project_name):
        """
        Assign a task to a user.
        """
        space = Space.objects.get(name=space_name)
        project = Project.objects.get(name=project_name, space__name=space_name)
        task = Task.objects.get(id=task_id)
        user = User.objects.get(email=request.data["email"])
        if user in task.project.get_members():
            task.assignee = user
            task.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ListRisks(APIView):
    def get(self, request, space_id, project_id):
        """
        Return a list of all tasks associated with a particular project.
        """
        risks = Risk.objects.filter(project=project_id)
        serializer = RiskSerializer(risks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateRisk(APIView):
    def post(self, request, space_id, project_id):
        """
        Create a new risk with provided credentials.
        """
        risk_serializer = RiskSerializer(data=request.data)
        if risk_serializer.is_valid(raise_exception=True):
            new_risk = risk_serializer.save()
            # risk_serializer.save()

            if new_risk:
                risks = Risk.objects.filter(project=project_id)
                serializer = RiskSerializer(risks, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(risk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateRisk(APIView):
    def put(self, request, risk_id):
        """
        Update a risk with provided credentials.
        """
        risk = Risk.objects.get(id=risk_id)
        risk_serializer = RiskSerializer(risk, data=request.data)
        if risk_serializer.is_valid(raise_exception=True):
            risk_serializer.save()
            return Response(risk_serializer.data, status=status.HTTP_200_OK)
        return Response(risk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteRisk(APIView):
    def delete(self, request, risk_id):
        """
        Delete a risk with provided credentials.
        """
        risk = Risk.objects.get(id=risk_id)
        risk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)