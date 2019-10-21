python

from selenium import webdriver


driver = ("C:\webdrivers\chromedriver")
driv = webdriver.Chrome(driver)
	

driv.get("http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx")

driv.get("http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx")


driv.implicitly_wait(20)
	
for x in range(12):
	ano = str(1 + x)
	driv.find_element_by_id("cphBody_listAno" + ano).click()
	driv.find_element_by_id("cphBody_ExportarBOLink").click()
	Print("cphBody_listAno" + ano)


