from django.db import models
from .utils import Utils


class Tree(models.Model):

    class Status(models.TextChoices):
        golden = 'g', 'Золотой'
        silver = 's', 'Серебрянный'

    TYPE = (
        ('n', 'Обычный'),
        ('a', 'Альтернативное')
    )

    def save(self, *args, **kwargs):
        pass
    def default_levels():
        return [1, 2, 3]

    levels = models.CharField(max_length=100, default=default_levels())
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя пользователя дерева', null=True, blank=True)
    description = models.TextField()
    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    balance = models.DecimalField(max_length=10, decimal_places=2)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    tree_type = models.CharField(max_length=1, choices=TYPE, default='n')
    status = models.CharField(max_length=1, choices=Status.choices, blank=Status.silver)

    # tree.balance tree.save()
    @property
    def utils(self):
        return Utils(self)

    @property
    def recivable_balance(self):
        return float(self.balance) * self.rate

    def calculate_balance(self):
        return float(self.balance) * self.rate

    class Meta:
        verbose_name = 'Дерево'
        ordering = ['-created_at']
        unique_together = ('name', 'email')


class Bonus(models.Model):

    amount = models.IntegerField()
    tree = models.ForeignKey('Tree', on_delete=models.CASCADE, null=True, blank=True, related_name='bonuses',
                             related_query_name='bonus')

