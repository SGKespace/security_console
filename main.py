import os
import django
from django.utils import timezone   # новое

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit

if __name__ == '__main__':
    # Программируем здесь
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    # cards = Passcard.objects.all()
    # active_cards = 0

    # active_cards = Passcard.objects.filter(is_active=True).count()
    # print('Активных пропусков ', active_cards)

    # visits = Visit.objects.all()

    # print(visits)

    # visits_not_leaved = Visit.objects.filter(leaved_at )

    def get_time_formatting(raw_time):
        time_seconds = raw_time.total_seconds()
        return '{:02}:{:02}:{:02}'.format(int(time_seconds // 3600),
                                   int(time_seconds % 3600 // 60),
                                   int(time_seconds % 60),
                                   )

    visits_not_leaved = Visit.objects.exclude(leaved_at__isnull=False)
    # print(visits_not_leaved)
    for visit in visits_not_leaved:
        print("Зашёл в хранилище, время по Москве:")
        # print(visits_not_leaved[0].entered_at)
        print(visit.entered_at)
        # print(timezone.localtime())
        print('Находится в хранилище:')
        # aaa = get_time_formatting(timezone.localtime() - visits_not_leaved[0].entered_at)
        work_time = get_time_formatting(timezone.localtime() - visit.entered_at)

        print(work_time)

