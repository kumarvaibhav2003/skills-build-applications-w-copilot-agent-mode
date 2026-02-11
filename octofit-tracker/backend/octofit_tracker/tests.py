from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel superheroes")
        self.user = User.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name="Web Swinging", description="Swing through the city")
        self.activity = Activity.objects.create(user=self.user, type="Cardio", duration=30, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)
        self.workout.suggested_for.add(self.user)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.team.name, "Marvel")

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(self.activity.user, self.user)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(self.leaderboard.team, self.team)

    def test_workout_suggestion(self):
        self.assertIn(self.user, self.workout.suggested_for.all())
