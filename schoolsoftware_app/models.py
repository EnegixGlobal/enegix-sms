from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
# -------------Login database---------------------------
class Department_loginDB(models.Model):
    email = models.EmailField(default="")
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
    
# -------------------------------Teacher Module---------------------------------
class Teacher(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Experience in years")
    employee_id = models.CharField(max_length=10, unique=True)
    joining_date = models.DateField(default=timezone.now)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return f"{self.name} ({self.employee_id})"


class TeacherAttendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
        ('Half-day', 'Half-day')
    ]

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)

    class Meta:
        unique_together = ('teacher', 'date')

    def __str__(self):
        return f"{self.teacher.name} - {self.date} - {self.status}"


class TeacherPayroll(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    month = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending')

    @property
    def total_salary(self):
        return self.basic_salary + self.allowances - self.deductions

    def __str__(self):
        return f"{self.teacher.name} - {self.month.strftime('%B %Y')} - {self.status}"


# -----------------------------------Students Module---------------------------- 
# -----------------------------------Class Model--------------------------------
class SchoolClass(models.Model):
    name = models.CharField(max_length=50)   # e.g., "Class 10"
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
        default='Active'
    )
    def __str__(self):
        return self.name

# -----------------------------------Section Model------------------------------
class Section(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=5)  # e.g., "A"
    def __str__(self):
        return f"{self.school_class.name} - {self.name}"
    
# ------------- -----
# TIMETABLE MODEL
# ------------------
class TimeTable(models.Model):
    DAYS = [
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
    ]

    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS)
    subject = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.school_class} {self.section} {self.day}"

class Parent(models.Model):
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.father_name} ({self.phone})"

class Student(models.Model):
    STATUS_CHOICES = [('Active','Active'), ('Inactive','Inactive')]
    name = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    photo = models.ImageField(upload_to='students/', blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)
    roll_no = models.CharField(max_length=20, blank=True)  
    admission_date = models.DateField(default=timezone.now)
    admission_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    barcode = models.ImageField(upload_to='student_barcodes/', blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} ({self.roll_no})"

class StudentAttendance(models.Model):
    ATT_CHOICES = [('Present','Present'), ('Absent','Absent'), ('Leave','Leave')]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=ATT_CHOICES)
    class Meta:
        unique_together = ('student','date')
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
    


# # ---------------- Fees Management ----------------
# class FeeStructure(models.Model):
#     class_name = models.CharField(max_length=50)
#     fee_type = models.CharField(max_length=50)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.class_name} - {self.fee_type}"


# # ---------------- Fee Collection ----------------
# class FeeCollection(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
#     paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     fine = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     payment_date = models.DateField(auto_now_add=True)
#     payment_mode = models.CharField(
#         max_length=20,
#         choices=[('Cash','Cash'),('Online','Online'),('Card','Card')]
#     )

#     def total_payable(self):
#         return self.fee_structure.amount - self.discount + self.fine

#     def __str__(self):
#         return self.student.name

# ---------------- FEE STRUCTURE ----------------
# class FeeStructure(models.Model):
#     school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
#     total_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.CharField(max_length=200, blank=True)
#     status = models.CharField(
#         max_length=10,
#         choices=[('Active','Active'),('Inactive','Inactive')],
#         default='Active'
#     )

#     def __str__(self):
#         return f"{self.school_class.name} - {self.total_fee}"


# # ---------------- FEE BILL / COLLECTION ----------------
# class FeeBill(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     fee_structure = models.ForeignKey(FeeStructure, on_delete=models.SET_NULL, null=True)
#     paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateField(auto_now_add=True)
#     payment_mode = models.CharField(
#         max_length=20,
#         choices=[('Cash','Cash'),('Online','Online'),('Cheque','Cheque')]
#     )
#     remark = models.CharField(max_length=200, blank=True)

#     def __str__(self):
#         return f"{self.student.name} - {self.paid_amount}"
    
# class FeePayment(models.Model):
#     bill = models.ForeignKey(FeeBill, on_delete=models.CASCADE, related_name='payments')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_mode = models.CharField(max_length=20)
#     payment_date = models.DateField()
#     remark = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

class FeeStructure(models.Model):
    school_class = models.ForeignKey('SchoolClass', on_delete=models.CASCADE)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
        default='Active'
    )

    def __str__(self):
        return f"{self.school_class.name} - {self.total_fee}"
    
class FeeBill(models.Model):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.PROTECT)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    # ✅ NEW (IMPORTANT)
    month = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES, null=True , blank=True
    )
    created_at = models.DateField(auto_now_add=True)

    def paid_amount(self):
        return self.payments.aggregate(total=Sum('amount'))['total'] or 0

    def pending_amount(self):
        return self.total_fee - self.paid_amount()
    
    def is_paid(self):
        return self.pending_amount() <= 0

    def status(self):
        return "Paid" if self.pending_amount() == 0 else "Pending"

    def __str__(self):
        return f"{self.student.name} - {self.total_fee}"


class FeeBillMonth(models.Model):
    bill = models.ForeignKey(FeeBill, related_name='months', on_delete=models.CASCADE)
    month = models.CharField(max_length=20)

    def __str__(self):
        return self.month



class FeePayment(models.Model):
    bill = models.ForeignKey(FeeBill, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(
        max_length=20,
        choices=[('Cash','Cash'), ('Online','Online'), ('Cheque','Cheque')]
    )
    payment_date = models.DateField()
    remark = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Exam(models.Model):
    name = models.CharField(max_length=100)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.school_class.name}"

# ---------------- SUBJECT RESULT ----------------
class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    max_marks = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"
    

class Homework(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    homework_file = models.FileField(upload_to='homework/', blank=True, null=True)
    due_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HomeworkSubmission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='homework_submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.homework.title}"

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    notice_date = models.DateField()

    def __str__(self):
        return self.title
    
# Transport Management
class Route(models.Model):
    name = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    monthly_fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    license_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=20)
    capacity = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.vehicle_no


class TransportAllocation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    # start_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.name} - {self.route.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=50, unique=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

from datetime import date

class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.PositiveIntegerField(default=0)
    is_returned = models.BooleanField(default=False)

    def calculate_fine(self):
        if not self.is_returned and self.due_date and date.today() > self.due_date:
            days_late = (date.today() - self.due_date).days
            return days_late * 10   # ₹10 per day
        return 0

    def __str__(self):
        return f"{self.book.title}"
    

# Warden Management
class Warden(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)
    join_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# ================= HOSTEL =================
class Hostel(models.Model):
    HOSTEL_TYPE_CHOICES = (
        ('Boys', 'Boys Hostel'),
        ('Girls', 'Girls Hostel'),
    )
    name = models.CharField(max_length=100)
    hostel_type = models.CharField(
        max_length=10,
        choices=HOSTEL_TYPE_CHOICES
    )
    address = models.TextField()
    warden = models.ForeignKey(Warden, on_delete=models.SET_NULL, null=True)
    total_rooms = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# ================= ROOM =================
class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    occupied = models.PositiveIntegerField(default=0)

    @property
    def remaining_beds(self):
        return self.capacity - self.occupied

    def __str__(self):
        return f"{self.room_no} ({self.hostel.name})"
    
# ================= ROOM ALLOCATION =================
class RoomAllocation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    allocated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.name
    
# ================= HOSTEL FEES =================
class HostelFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE ,null=True,blank=True)  
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.month}"

    
    

