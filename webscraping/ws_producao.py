import requests
from bs4 import BeautifulSoup

url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="tb_base tb_dados")

dados_producao = []

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    line = [col.get_text(strip=True) for col in cols]
    dados_producao.append(line)
    