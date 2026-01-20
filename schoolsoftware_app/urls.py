from django.urls import path
from schoolsoftware_app.views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # Teacher Management
    path('all/', all_teachers, name='all_teachers'),
    path('add/', add_teacher, name='add_teacher'),
    path('edit-teacher/<int:id>/', edit_teacher, name='edit_teacher'),
    path('delete-teacher/<int:id>/', delete_teacher, name='delete_teacher'),
    path('attendance/', teacher_attendance, name='teacher_attendance'),
    path('attendance/update/', update_teacher_attendance, name='update_teacher_attendance'),
    path('attendance/export/', export_teacher_attendance_excel, name='export_teacher_attendance_excel'),
    path('teachers/attendance/export/pdf/',export_teacher_attendance_pdf,name='export_teacher_attendance_pdf'),
    path('payroll/', teacher_payroll, name='teacher_payroll'),
    path('payroll/generate/', generate_payroll, name='generate_payroll'),
    path('payroll/status/<int:payroll_id>/', update_payroll_status, name='update_payroll_status'),

    # --------------------------Student Module----------------------------------
    path('students/', all_students, name='all_students'),
    path('students/add/', add_student, name='add_student'),
    path('students/edit/<int:id>/', edit_student, name='edit_student'),
    path('students/delete/<int:id>/', delete_student, name='delete_student'),

    path('students/promotion/', student_promotion, name='student_promotion'),
    path('students/promotion/apply/', apply_promotion, name='apply_promotion'),

    path('students/attendance/', student_attendance, name='student_attendance'),
    path('students/attendance/export/', export_attendance_excel, name='export_attendance_excel'),

    path('students/id-cards/', student_id_cards, name='student_id_cards'),
    path('students/id-cards/download/', download_id_cards_pdf, name='download_id_cards_pdf'),
    path('students/<int:id>/', student_detail, name='student_detail'),
    path('student/<int:id>/',student_qr_profile, name='student_qr_profile'),

    path('students/export/excel/', export_students_excel, name='export_students_excel'),
    path('students/export/pdf/', export_students_pdf, name='export_students_pdf'),


     # CLASS
    path('classes/', class_list, name='class_list'),
    path('classes/add/', add_class, name='add_class'),
    path('classes/edit/<int:id>/', edit_class, name='edit_class'),
    path('classes/delete/<int:id>/', delete_class, name='delete_class'),

    #SECTION
    path('sections/', section_list, name='section_list'),
    path('sections/add/', add_section, name='add_section'),
    path('sections/edit/<int:id>/', edit_section, name='edit_section'),
    path('sections/delete/<int:id>/', delete_section, name='delete_section'),

    # TIMETABLE
    path('timetable/', timetable_list, name='timetable_list'),
    path('timetable/add/', add_timetable, name='add_timetable'),
    path('timetable/edit/<int:id>/', edit_timetable, name='edit_timetable'),
    path('timetable/delete/<int:id>/', delete_timetable, name='delete_timetable'),

    # ----------------------Fees Management------------------------------------

    # path('fee-structure/', fee_structure_list, name='fee_structure_list'),
    # path('fee-structure/add/', fee_structure_add, name='fee_structure_add'),

    # path('fee-billing/', fee_bill_list, name='fee_bill_list'),
    # path('fee-billing/add/', fee_bill_add, name='fee_bill_add'),

    # path('fees/collect/<int:bill_id>/', collect_fee, name='collect_fee'),
    # path('pending-fees/', pending_fees, name='pending_fees'),

     # Fee Structure
    path('fee-structure/', fee_structure_list, name='fee_structure_list'),
    path('fee-structure/add/', fee_structure_add, name='fee_structure_add'),

    # Fee Billing
    path('fee-billing/', fee_bill_list, name='fee_bill_list'),
    path('fee-billing/add/', fee_bill_add, name='fee_bill_add'),
    path('fee-receipt/<int:bill_id>/',fee_receipt_download,name='fee_receipt_download'),
    path('fees/get-paid-months/<int:student_id>/', get_paid_months, name='get_paid_months'),
    path('ajax/get-students/', get_filtered_students, name='get_filtered_students'),
    path('fee-structure/edit/<int:id>/', fee_structure_edit, name='fee_structure_edit'),
    # path('fee-structure/delete/<int:id>/', fee_structure_delete, name='fee_structure_delete'),

    # Payments
    path('fees/collect/<int:bill_id>/', collect_fee, name='collect_fee'),

    # Reports
    path('pending-fees/', pending_fees, name='pending_fees'),

    #Exam Management
    path('exams/', exam_list, name='exam_list'),
    path('exams/add/', add_exam, name='add_exam'),
    path('exams/<int:exam_id>/upload/', upload_result, name='upload_result'),
    path('report-card/<int:student_id>/<int:exam_id>/', report_card, name='report_card'),

    #Homework Management
    path('homework/', homework_list, name='homework_list'),
    path('homework/add/', add_homework, name='add_homework'),
    path('homework/edit/<int:pk>/', edit_homework, name='edit_homework'),
    path('homework/delete/<int:pk>/', delete_homework, name='delete_homework'),

    #Notice Management
    path('notice/', notice_list, name='notice_list'),
    path('notice/add/', add_notice, name='add_notice'),
    path('notice/edit/<int:pk>/', edit_notice, name='edit_notice'),
    path('notice/delete/<int:pk>/', delete_notice, name='delete_notice'),

    # Transport Management
    path('transport/routes/', route_list, name='route_list'),
    path('transport/routes/add/', route_add, name='route_add'),

    path('transport/drivers/', driver_list, name='driver_list'),
    path('transport/drivers/add/', driver_add, name='driver_add'),

    path('transport/vehicles/', vehicle_list, name='vehicle_list'),
    path('transport/vehicles/add/', vehicle_add, name='vehicle_add'),

    path('transport/allocation/', allocation_list, name='allocation_list'),
    path('transport/allocation/add/', allocation_add, name='allocation_add'),

    # Transport Management
    # ROUTE
    path('routes/edit/<int:id>/', route_edit, name='route_edit'),
    path('routes/delete/<int:id>/', route_delete, name='route_delete'),

    # DRIVER
    path('drivers/edit/<int:id>/', driver_edit, name='driver_edit'),
    path('drivers/delete/<int:id>/', driver_delete, name='driver_delete'),

    # VEHICLE
    path('vehicles/edit/<int:id>/', vehicle_edit, name='vehicle_edit'),
    path('vehicles/delete/<int:id>/', vehicle_delete, name='vehicle_delete'),

    # ALLOCATION
    path('allocations/edit/<int:id>/', allocation_edit, name='allocation_edit'),
    path('allocations/delete/<int:id>/', allocation_delete, name='allocation_delete'),

    #Library Management
    path('library/books/',book_list, name='book_list'),
    path('library/books/add/',book_add, name='book_add'),
    path('library/books/edit/<int:id>/',book_edit, name='book_edit'),
    path('library/books/delete/<int:id>/',book_delete, name='book_delete'),

    path('library/issue/',issue_list, name='issue_list'),
    path('library/issue/add/',issue_book, name='issue_book'),
    path('library/return/<int:id>/',return_book, name='return_book'),

    #Warden Management
    path('warden/list', warden_list, name='warden_list'),
    path('add/warden', warden_add, name='warden_add'),
    path('edit/<int:id>/', warden_edit, name='warden_edit'),
    path('delete/<int:id>/', warden_delete, name='warden_delete'),

    #  # HOSTEL
    # path('hostels/', hostel_list, name='hostel_list'),
    # path('hostels/add/', hostel_add, name='hostel_add'),
    # path('hostels/edit/<int:id>/', hostel_edit, name='hostel_edit'),

    # HOSTEL
    path('hostel/', hostel_list, name='hostel_list'),
    path('hostel/add/', hostel_form, name='hostel_add'),
    path('hostel/edit/<int:id>/', hostel_form, name='hostel_edit'),
    path('hostel/delete/<int:id>/', hostel_delete, name='hostel_delete'),

    # ROOMS
    path('rooms/', room_list, name='room_list'),
    path('rooms/add/', room_form, name='room_add'),
    path('rooms/edit/<int:id>/', room_form, name='room_edit'),
    path('rooms/delete/<int:id>/', room_delete, name='room_delete'),

    # ALLOCATION
    # path('allocation/', allocation_list, name='allocation_list'),
    # path('allocation/add/', allocation_form, name='allocation_add'),
    # path('allocation/delete/<int:id>/', allocation_delete, name='allocation_delete'),

    # ROOM ALLOCATION
    path('room-allocation/', room_allocation_list, name='room_allocation_list'),
    path('room-allocation/add/', room_allocation_add, name='room_allocation_add'),
    path('room-allocation/edit/<int:id>/', room_allocation_list, name='room_allocation_edit'),
    path('room-allocation/delete/<int:id>/', room_allocation_delete, name='room_allocation_delete'),

    # FEES
    path('fees/', fee_list, name='hostel_fee_list'),
    path('fees/add/', fee_form, name='hostel_fee_add'),
    path('fees/delete/<int:id>/', fee_delete, name='hostel_fee_delete'),

]
