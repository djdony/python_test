from django.db import models


class Poll(models.Model):
    """Атрибуты опроса: название, дата старта, дата окончания, описание. """
    title = models.CharField(max_length=200, verbose_name="Название")
    text = models.TextField(max_length=200, verbose_name="Описание")
    date_start = models.DateTimeField(verbose_name="Дата старта")
    date_end = models.DateTimeField(verbose_name="Дата окончания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    question_type = (
        ('M', 'ответ с выбором нескольких вариантов'),
        ('S', 'ответ с выбором одного варианта'),
        ('T', 'ответ текстом'),
    )
    """Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)"""
    text = models.TextField(max_length=200, verbose_name="Текст Вопроса")
    question_type = models.CharField(max_length=1,
                                         verbose_name="Тип вопроса",
                                         null=False,
                                         choices=question_type,
                                         default=None,
                                         blank=False)
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT, related_name='question')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)"""
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='answer')
    title = models.CharField(max_length=200, verbose_name="Ответ")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
