from django.db import models


class Airman(models.Model):
    RANK_CHOICE = (
        ('AB', 'AB'),
        ('AMN', 'Amn'),
        ('A1C', 'A1C'),
        ('SRA', 'SrA'),
        ('SSGT', 'SSgt'),
        ('TSGT', 'TSgt'),
        ('MSGT', 'MSgt'),
        ('SMSGT', 'SMSgt'),
        ('CMSGT', 'CMSgt'),
        ('2ND LT', '2nd Lt'),
        ('1ST LT', '1st Lt'),
        ('CAPT', 'Capt'),
        ('MAJ', 'Maj'),
        ('LT COL', 'Lt Col'),
        ('COL', 'Col'),
        ('BRIG GEN', 'Brig Gen'),
        ('MAJ GEN', 'Maj Gen'),
        ('LT GEN', 'Lt Gen'),
        ('GEN', 'General'),
    )
    FITNESS_CHOICE = (
        ('excellent', 'EXCELLENT'),
        ('satisfactory', 'SATISFACTORY'),
        ('pass', 'PASS'),
        ('unsatisfactory', 'UNSATISFACTORY'),
        ('fail', 'FAIL'),
        ('exemption', 'EXEMPTION'),
    )
    airman_id = models.AutoField(primary_key=True, serialize=True)
    fitness_level = models.CharField(max_length=50,
                                     choices=FITNESS_CHOICE,
                                     default='satisfactory')
    rank = models.CharField(max_length=10,
                            choices=RANK_CHOICE,
                            default='ab')
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=5)
    last_name = models.CharField(max_length=50)
    ssn = models.IntegerField()
    airman_slug = models.SlugField(max_length=9,
                                   unique_for_date='test_date')
    test_date = models.DateField()
    ptl = models.BooleanField(default=False)
    ufpm = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rank} {self.first_name} {self.middle_initial} {self.last_name}"


class Failure(models.Model):
    failure_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.DO_NOTHING, )
    failure_date = models.DateField()
    be_well_completion_date = models.DateField()

    def __str__(self):
        return f"{self.airman_id}: Failure date on {self.failure_date}"


class Physical_Training_Leader(models.Model):
    ptl_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.DO_NOTHING, )
    ptl_certification_date = models.DateField()
    ptl_expiration_date = models.DateField()
    cpr_expiration_date = models.DateField()

    def __str__(self):
        return f"{self.airman_id}: Certified on {self.ptl_certification_date} and expires on {self.ptl_expiration_date}"


class Unit_Fitness_Program_Manager(models.Model):
    ufpm_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.DO_NOTHING, )
    ptl_id = models.ForeignKey(
        Physical_Training_Leader,
        on_delete=models.CASCADE, )
    ufpm_certification_date = models.DateField()
    ufpm_expiration_date = models.DateField()

    def __str__(self):
        return f"{self.airman_id}, Certified on {self.ufpm_certification_date} and expires on {self.ufpm_expiration_date}"


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.DO_NOTHING, )
    profile_start_date = models.DateField()
    profile_expiration_date = models.DateField()
    profile_details = models.TextField()

    def __str__(self):
        return f"{self.airman_id}: Profile Expiration Date: {self.profile_expiration_date}"
