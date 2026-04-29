from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')

        # Create Activities
        Activity.objects.create(user=tony, type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Running', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Running', duration=60, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=150, rank=1)
        Leaderboard.objects.create(user=steve, score=120, rank=2)
        Leaderboard.objects.create(user=clark, score=110, rank=3)
        Leaderboard.objects.create(user=bruce, score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
