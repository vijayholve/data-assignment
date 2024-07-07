
class Command(BaseCommand):
    help = 'Check database connection'

    def handle(self, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                row = cursor.fetchone()
            if row:
                self.stdout.write(self.style.SUCCESS('Database connection successful'))
            else:
                self.stdout.write(self.style.ERROR('Database connection failed'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Database connection error: {e}'))