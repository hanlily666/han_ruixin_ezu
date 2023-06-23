from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year


class CourseInfoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="tester", email="", password="{iSchoolUI}")
        cls.period = Period.objects.create(period_sequence="1", period_name="Spring")
        cls.year = Year.objects.create(year="2020")
        cls.semester = Semester.objects.create(year=cls.year, period=cls.period,)
        cls.course = Course.objects.create(course_number=cls.course_number_, course_name=cls.course_name_,)
        cls.instructor = Instructor.objects.create(first_name="Kevin", last_name="Trainer", disambiguator="Harvard")
        cls.student = Student.objects.create(first_name="Ruixin", last_name="Han", disambiguator="UIUC")
        cls.section = Section.objects.create(section_name="AOG/AOU", semester=cls.semester, course=cls.course, instructor=cls.instructor)
        cls.registration = Registration.objects.create(student=cls.student, section=cls.section)

    def test_period_model(self):
        self.assertEqual(self.period.period_sequence, "1")
        self.assertEqual(self.period.period_name, "Spring")

    def test_year_model(self):
        self.assertEqual(self.year.year, "2020")

    def test_semester_model(self):
        self.assertEqual(self.semester.year, self.year)
        self.assertEqual(self.semester.period, self.period)
    #
    # def test_course_model(self):
    #     self.assertEqual(self.course.course_number, "IS430")
    #     self.assertEqual(self.course.course_name, "Foundation of Information Processing")
    #
    # def test_instructor_model(self):
    #     self.assertEqual(self.instructor.first_name, "Kevin")
    #     self.assertEqual(self.instructor.last_name, "Trainer")
    #     self.assertEqual(self.instructor.disambiguator, "Harvard")
    #
    # def test_student_model(self):
    #     self.assertEqual(self.student.first_name, "Ruixin")
    #     self.assertEqual(self.student.last_name, "Han")
    #     self.assertEqual(self.student.disambiguator, "UIUC")
    #
    # def test_section_model(self):
    #     self.assertEqual(self.section.section_name, "AOG/AOU")
    #     self.assertEqual(self.section.semester, self.year_, self.period_)
    #     self.assertEqual(self.section.course, self.course_)
    #     self.assertEqual(self.section.instructor, self.instructor_)
    #
    # def test_registration_model(self):
    #     self.assertEqual(self.registration.student, self.student_)
    #     self.assertEqual(self.registration.section, self.section_)

    # def test_url_exists_at_correct_location_listview(self):  # new
    #     response = self.client.get("/")
    #     self.assertEqual(response.status_code, 200)

    # def test_course_listview(self):
    #     response = self.client.get(reverse("course"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Nice body content")
    #     self.assertTemplateUsed(response, "course.html")
    #
    # def test_instructor_list_listview(self):
    #     response = self.client.get(reverse("instructor_list"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, self.instructor_)
    #     self.assertTemplateUsed(response, "instructor_list.html")
    #
    # def test_registration_listview(self):
    #     response = self.client.get(reverse("registration"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, self.student_, self.section_)
    #     self.assertTemplateUsed(response, "registration.html")
    #
    # def test_section_listview(self):
    #     response = self.client.get(reverse("section"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Nice body content")
    #     self.assertTemplateUsed(response, "instructor_list.html")