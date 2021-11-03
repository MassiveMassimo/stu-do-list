from django.test import Client, TestCase

# Create your tests here.

# class TestSchedule(TestCase):

    # def test_uniform_resource_locator(self):
    #     resp = Client().get('/jadwal-belajar-bareng/')
    #     self.assertEquals(200, resp.status_code)

    # def test_form(self):
    #     resp = Client().get('/jadwal-belajar-bareng/add/')
    #     konten = resp.content.decode('utf8')
    #     self.assertIn('<form action="" method="POST">', konten)

    # def test_isi(self):
    #     resp = Client().get('/jadwal-belajar-bareng/')
    #     konten = resp.content.decode('utf8')
    #     self.assertIn("Mata Kuliah", konten)
    #     self.assertIn("Tanggal", konten)
    #     self.assertIn("Waktu", konten)
    #     self.assertIn("Topik", konten)
    #     self.assertIn("Informasi", konten)
    #     self.assertIn("Link", konten)
