import uuid

import factory
from factory import fuzzy
from faker import Factory

from . import models

factory_ru = Factory.create('ru_RU')


class Applicant(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    last_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    middle_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    birthdate = factory.Sequence(lambda n: factory_ru.date())
    health_status = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    phone_number = factory.Sequence(lambda n: factory_ru.phone_number())
    gender = fuzzy.FuzzyChoice(i for i in ['Мужчина', 'Женщина'])
    image = factory.Sequence(lambda n: factory_ru.image_url())

    class Meta:
        model = models.Applicant


class EmergencyService(factory.django.DjangoModelFactory):
    service_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    service_code = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=50))
    phone_number = factory.Sequence(lambda n: factory_ru.phone_number())

    class Meta:
        model = models.EmergencyService


class Request(factory.django.DjangoModelFactory):
    request_number = factory.Sequence(lambda n: str(uuid.uuid4()))
    request_date = factory.Sequence(lambda n: factory_ru.date())
    injured = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=50))
    do_not_call = fuzzy.FuzzyChoice(i for i in ['Да', 'Нет'])
    status = fuzzy.FuzzyChoice(i for i in ['В работе', 'Завершено'])
    applicant = factory.SubFactory(Applicant)

    class Meta:
        model = models.Request

    @factory.post_generation
    def emergency_service(self, create: bool, extracted: bool, **kwargs: dict) -> None:
        if not create:
            return
        if extracted:
            for service in extracted:
                self.emergency_service.add(service)
        else:
            self.emergency_service.add(EmergencyService())
