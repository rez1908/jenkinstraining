from selenium import webdriver

def test_setup():
	global driver
	driver = webdriver.Chrome(executable_path ="C:/driver/chromedriver.exe")
	driver.maximize_window()

def test_from_entry():
	driver.get("http://localhost/sample_web_app/form.php")
	driver.find_element_by_name("nip").send_keys("12345")
	driver.find_element_by_name("nama").send_keys("John Wick")
	driver.find_element_by_name("nik").send_keys("14110944")
	driver.find_element_by_name("alamat").send_keys("Tangerang")
	driver.find_element_by_name("perusahaan").send_keys("Fiktif Inc")
	driver.find_element_by_name("tanggal").send_keys("01/01/2021")
	driver.find_element_by_name("divisi").send_keys("hrd")
	driver.find_element_by_name("posisi").send_keys("staff")
	driver.find_element_by_name("gaji").send_keys("100000")
	driver.find_element_by_name("atasan").send_keys("Rudi S")
	driver.find_element_by_name("submit").click()

def test_cleanup():
	driver.close()
	driver.quit()
	print("Test Selesai...")