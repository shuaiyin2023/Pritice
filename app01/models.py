from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True


class Person(BaseModel):
    name = models.CharField(max_length=20, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(verbose_name="邮箱")
    number = models.CharField(max_length=20, verbose_name="电话号码")
    address = models.CharField(max_length=50, verbose_name="地址")

    class Meta:
        verbose_name = "人员信息"
        verbose_name_plural = verbose_name


class Student(BaseModel):
    name = models.CharField(max_length=20, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(verbose_name="邮箱")
    number = models.CharField(max_length=20, verbose_name="电话号码")

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name


class Teacher(BaseModel):
    name = models.CharField(max_length=20, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(verbose_name="邮箱")
    number = models.CharField(max_length=20, verbose_name="电话号码")

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name


class Course(BaseModel):
    name = models.CharField(max_length=20, verbose_name="课程名称")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="教师")
    student = models.ManyToManyField(Student, related_name="course_student", verbose_name="学生")
    start_time = models.DateTimeField(verbose_name="开课时间")
    end_time = models.DateTimeField(verbose_name="结课时间")
    place = models.CharField(max_length=50, verbose_name="上课地点")

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name
