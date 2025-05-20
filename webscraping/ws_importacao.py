import requests
from bs4 import BeautifulSoup

urls = [
    'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05',
    'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05',
    'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05',
    'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05',
    'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05',
    'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05'
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="tb_base tb_dados")

    dados_importacao = []

    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        line = [col.get_text(strip=True) for col in cols]
        dados_importacao.append(line)
    