

from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import QuestionSerializer,AnswerSerializer
from questions.models import Answer, Question


class QuestionViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Questions."""

    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# /questions/slug/answer/

class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request)
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        print(kwarg_slug)
        question = get_object_or_404(Question,slug=kwarg_slug)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered the question!!")
        serializer.save(author = request_user,question = question)



class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]
    lookup_field = "uuid"


class AnswerListAPIView(generics.ListAPIView):
    serializer_class =AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug = kwarg_slug).order_by("-created_at")

