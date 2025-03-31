import streamlit as st
import sqlite3
import pandas as pd
import os
import plotly.express as px
import shutil
import zipfile
import tempfile
from io import BytesIO
import hashlib
import streamlit as st
import sqlite3
import hashlib
import webbrowser
import os
import pandas as pd
import sqlite3
import streamlit as st
import urllib.parse
import sqlite3
import os
from datetime import date
from datetime import datetime



# Conectar ao banco de dados
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Criar tabela de usuários se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    empresas TEXT,
                    permissoes TEXT)''')
conn.commit()

# Lista de empresas disponíveis
lista_empresas = ["2B COMBUSTIVEL LTDA", "A REDE GESTAO PATRIMONIAL LTDA", "A.M CHEQUER IMOVEIS LTDA", "A.R. PARTICIPACOES LTDA", "ABEL CONSTRUTORA LTDA", "ABEL SEMINOVOS LTDA", "ACOLOG LOGISTICA LTDA", "ACOS SERVICOS DE PROMOCAO LTDA", "ACR GESTAO PATRIMONIAL LTDA", "ADCAR SERVICO DE ESCRITORIO E APOIO ADMINISTRATIVO LTDA", "ADR MOBILIDADE E SERVICOS LTDA", "ADS COMERCIO E IMPORTACAO E EXPORTACAO EIRELI", "AESA PARTICIPAÇÕES LTDA", "AGM ESQUADRIAS LTDA", "AGP03 EMPREENDIMENTOS IMOBILIARIOS SPE LTDA", "AGP03 EMPREENDIMENTOS IMOBILIARIOS SPE LTDA FILIAL 02-82", "AGP03 EMPREENDIMENTOS IMOBILIARIOS SPE LTDA SCP RESIDENCIAL CAPARAO", "AGP05 ARGON EMPREENDIMENTOS IMOBILIARIOS SPE LTDA", "AGROPECUARIA BONANZA LTDA", "AGT01 MORADA NOVA DE MINAS SPE LTDA", "AGT01 MORADA NOVA DE MINAS SPE LTDA FILIAL 02-52", "AGUIA 8 COMERCIO DE COMBUSTIVEIS LTDA", "AGUIA IV COMERCIO DE COMBUSTIVEIS LTDA", "AGUIA IX COMERCIO DE COMBUSTIVEIS LTDA", "AGUIA V COMERCIO DE COMBUSTIVEIS LTDA", "ALLOTECH CONSULTORIA EM PRODUCAO INDUSTRIAL LTDA", "ALVES E SANTOS PARTICIPACOES LTDA", "AMH COMERCIO E SERVICOS LTDA", "AML HOLDING S/A", "AMMC PARTICIPACOES LTDA", "AMPLUS PARTICIPACOES SA", "AMX GESTÃO PATRIMONIAL LTDA", "ANF EMPREENDIMENTOS E PARTICIPACOES LTDA", "ANITA CHEQUER PARTICIPACOES LTDA", "ANITA CHEQUER PATRIMONIAL LTDA", "APL ADMINISTRACAO E PARTICIPACOES LTDA", "APMG PARTICIPACOES S/A", "ARCI PARTICIPACOES LTDA", "ARCI PATRIMONIAL LTDA", "ARGON ENGENHARIA LTDA", "ARNDT PATRIMONIAL LTDA", "ARNDT REFORMAS E MANUTENCOES LTDA", "ARNDT, TRAVASSOS E MORRISON SPE LTDA", "ARTMIX HOLDING LTDA", "AUMAR PRESTACAO DE SERVICOS ADMINISTRATIVOS LTDA", "AUTO POSTO ALELUIA LTDA", "AUTO POSTO ALELUIA LTDA FILIAL 02-46", "AUTO POSTO CENTENARIO LTDA", "AUTO POSTO DAS LAJES LTDA", "AUTO POSTO DOM BOSCO LTDA", "AUTO POSTO MAQUINE LTDA", "AUTO POSTO MARIO CAMPOS COMERCIO DE COMBUSTIVEIS LTDA", "AUTO POSTO PORTAL DO NORTE LTDA", "AUTO POSTO VERONA LTDA", "AUTOREDE LOCADORA DE VEICULOS LTDA", "AUTOREDE PARTICIPACOES LTDA", "AXJ PARTICIPACOES EIRELI", "AXP GESTAO PATRIMONIAL LTDA", "AZEVEDO & CIA", "BARAO VPP CONVENIENCIAS LTDA", "BARTELS DERMATOLOGIA ESTETICA E LASER LTDA", "BEL DISTRIBUIDOR DE LUBRIFICANTES LTDA", "BEL DISTRIBUIDOR DE LUBRIFICANTES LTDA FILIAL 02-79", "BEL LUBRIFICANTES ESPECIAIS LTDA", "BELTMORE PARTICIPACOES LTDA", "BEMX - PARTICIPACOES E EMPREENDIMENTOS LTDA", "BIOCLINTECH CIENTIFICA LTDA", "BIOCLINTECH LTDA", "BIOCLINTECH MANUTENCAO LTDA", "BLUE SKY PARTICIPACOES LTDA", "BMC EDITORA LTDA", "BMGL PARTICIPACOES E EMPREENDIMENTOS IMOBILIARIOS LTDA", "BOA VISTA ASSESSORIA LTDA", "BOA VISTA BOCAIUVA HOTEL LTDA", "BORA EMBALAGENS LTDA", "BRANT EMPREENDIMENTOS LTDA", "BRASIL CONCRETO LTDA", "BRAZIL MANIA LTDA", "BRB TRANSPORTES LTDA", "BRM COMERCIO DE VEICULOS LTDA", "BRM COMERCIO DE VEICULOS LTDA FILIAL 02-24", "BROMELIAS GESTAO PATRIMONIAL LTDA", "BURITIS CONVENIENCIA LTDA", "BV DISTRIBUIDORA LTDA", "CAD COMERCIAL DE MAQUINAS LTDA", "CAMPO ALEGRE PARTICIPACOES LTDA", "CAPITAO COMERCIO DE COMBUSTIVEIS LTDA", "CASA NOVA SPE LTDA", "CASA SEMPRE VIVA COMERCIO DE MATERIAIS DE CONSTRUCAO LTDA", "CASCALHO PARTICIPACOES LTDA", "CATIRA INTERMEDIACOES DE NEGOCIOS LTDA", "CCA COMERCIAL DE COMBUSTIVEIS AUTOMOTIVOS LTDA", "CDI NUCLEAR LTDA", "CDVM LTDA", "CELT -COMERCIO DE COMBUSTIVEIS E LUBRIFICANTES LTDA", "CENTER POSTO LTDA", "CENTER POSTO LTDA FILIAL 02-12", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 02-49", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 04-00", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 05-91", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 07-53", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 09-15", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 10-59", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 11-30", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 14-82", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 17-25", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 19-97", "CENTRO DE DIAGNOSTICO POR IMAGEM LTDA FILIAL 20-20", "CGA SERVICOS MEDICOS LTDA", "CGI - EMPREENDIMENTOS COMERCIAL LTDA", "CHAVE DE OURO EMPREENDIMENTOS IMOBILIARIOS EIRELI", "CHEL LTDA", "CHEQUER & COELHO LTDA", "CIA ITABIRITO INDUSTRIAL FIACAO E TECELAGEM DE ALGODAO", "CIAZA CONSTRUTORA LTDA", "CLAM CONSULTORIA LTDA", "CLAM ENGENHARIA LTDA", "CLAM ENGENHARIA LTDA FILIAL 03-00", "CLAM ESG LTDA", "CLAM MEIO AMBIENTE LTDA", "CLAM MEIO AMBIENTE LTDA FILIAL 02-49", "CLAM MONITORAMENTO AMBIENTAL LTDA", "CLAM MONITORAMENTO AMBIENTAL LTDA", "CLAM PARTICIPACOES E INVESTIMENTOS S/A", "CLINICA LEV SAVASSI LTDA", "CLINICA RADIOLOGICA ELDORADO LTDA", "CLINICA UNIAO SERVICOS MEDICOS LTDA", "COELHO CONVENIENCIA LTDA", "COELHO E PEREIRA EIRELI", "COLISEU SERVICOS ADMINISTRATIVOS LTDA", "COMERCIAL AVIAMENTOS LTDA", "COMERCIAL FOCCUS LTDA", "COMERCIAL GIULIANO LIMITADA", "COMERCIAL OLIVEIRA & BRANT LTDA", "COMERCIAL OLIVEIRA & BRANT LTDA", "COMERCIO LANCHE KARRAO LTDA", "CONSORCIO ENGEBRAS ILCON SES 0620240094", "CONSORCIO GERASUN SOLAR", "CONSTANTINO MATIAS NOGUEIRA - IMOVEIS", "CONSTANTINO MATIAS NOGUEIRA - PATRIMONIAL LTDA", "CONSTRUTORA AGMAR LTDA", "CONSTRUTORA AGMAR LTDA", "CONSTRUTORA AGMAR LTDA FILIAL 02-10", "CONSTRUTORA E INCORPORADORA SPLIT LTDA", "CONTABILIDADE LTDA", "CONVENIENCIA DOIS IRMAOS - EIRELI", "CONVENIENCIA DOIS IRMAOS LTDA", "CORRETORA DE SEGUROS BELO HORIZONTE LTDA", "CRISTAL VALLE ADMINISTRACAO LTDA", "CRISTAL VALLE INDUSTRIA E COMERCIO DE VIDROS LTDA", "CSV GESTAO PATRIMONIAL LTDA", "CVQ I SPE LTDA", "CVQ II SPE LTDA", "D.L.A. SERVICOS ADMINISTRATIVOS LTDA", "DEBURR COMERCIO DE COSMETICOS LTDA", "DEL PAPEIS LTDA", "DEL PAPEIS LTDA FILIAL 03-84", "DELMA - COMERCIO DE COMBUSTIVEIS LTDA", "DH ORIGINAL IMPORTACAO E EXPORTACAO LTDA", "DISTRIBUIDORA BIOCLIN DIAGNOSTICA LTDA", "DJB PARTICIPACOES LTDA", "DOBRAFLEX CORTE E DOBRA DE METAIS LTDA", "DVS PARTICIPACOES LTDA", "E.D. TECNOLOGIA DIGITAL BH LTDA", "EAGLE ADMINISTRACAO LTDA", "EDIFICIO REDE OFFICE I", "ELETROFERRAGENS RM EIRELI", "EMAG CONSTRUTORA LTDA", "EMAG CONSTRUTORA LTDA", "EMIS MINAS DISTRIBUIDORA DE PRODUTOS FARMACEUTICOS LTDA", "EMP - AVALIACAO EM RECURSOS HUMANOS LTDA", "EMPIRE DJB PATRIMONIAL LTDA", "ENERGY TRANSPORTES LTDA", "ENGEBRAS CONSTRUTORA LTDA", "ESMIG INDUSTRIA DE ESCADAS LTDA", "ESMIG INDUSTRIA DE ESCADAS LTDA FILIAL 03-89", "ESTACIONAMENTO AGMAR LTDA", "ESTACIONAMENTO AGMAR LTDA FILIAL 02-06", "ESTACIONAMENTO AGMAR LTDA FILIAL 03-89", "ESTACIONAMENTO AGMAR LTDA FILIAL 04-60", "ESTIVA PARTICIPACOES LTDA","EAT FRUTZ ALIMENTOS LTDA" , "EVELINE DE PAULA BARTELS", "EVERYBODY - CENTRO DE PERFORMANCE E FISIOTERAPIA LTDA", "EVOLUTION CONSULTORIA E GESTAO EMPRESARIAL S/A", "EXPRESSO FERRENSE LTDA", "FAST GESTAO DE RECURSOS LTDA", "FAST TEAM SERVICOS DE ESTETICA AUTOMOTIVA LTDA", "FASTPLOT SERVICOS DE ESTETICA AUTOMOTIVA LTDA", "FATIMA ADMINISTRACAO LTDA", "FCF CONSULTORIA LTDA", "FCK PREMOLDADOS LTDA FILIAL 02", "FCK PREMOLDADOS LTDA FILIAL 03", "FCK PREMOLDADOS LTDA", "FCK TRANSPORTES LTDA", "FEAG - FERRAGENS AGMAR PARA FACHADA EIRELI", "FERREIRA ADMINISTRACAO LTDA", "FERRO E ACO TAKONO LTDA", "FERRO E ACO TAKONO LTDA FILIAL 0028-03", "FERRO E ACO TAKONO LTDA FILIAL 06-06", "FERRO E ACO TAKONO LTDA FILIAL 07-89", "FERRO E ACO TAKONO LTDA FILIAL 08-60", "FERRO E ACO TAKONO LTDA FILIAL 10-84", "FERRO E ACO TAKONO LTDA FILIAL 11-65", "FERRO E ACO TAKONO LTDA FILIAL 12-46", "FERRO E ACO TAKONO LTDA FILIAL 13-27", "FERRO E ACO TAKONO LTDA FILIAL 14-08", "FERRO E ACO TAKONO LTDA FILIAL 15-99", "FERRO E ACO TAKONO LTDA FILIAL 16-70", "FERRO E ACO TAKONO LTDA FILIAL 18-31", "FERRO E ACO TAKONO LTDA FILIAL 19-12", "FERRO E ACO TAKONO LTDA FILIAL 20-56", "FERRO E ACO TAKONO LTDA FILIAL 21-37", "FERRO E ACO TAKONO LTDA FILIAL 22-18", "FERRO E ACO TAKONO LTDA FILIAL 23-07", "FERRO E ACO TAKONO LTDA FILIAL 24-80", "FERRO E ACO TAKONO LTDA FILIAL 25-60", "FERRO E ACO TAKONO LTDA FILIAL 26-41", "FERRO E ACO TAKONO LTDA FILIAL 27-22", "FIX MANUTENCAO PREDIAL LTDA", "FIX MANUTENCOES LTDA", "FLARA GESTAO PATRIMONIAL LTDA", "FMPL PARTICIPACOES LTDA", "FORTRESS GESTAO PARTICIPACOES LTDA", "FRADE PARTICIPACOES LTDA", "FS PROCESSAMENTO DE DADOS LTDA", "GAMA SERV LTDA", "GECORP GESTAO DE BENEFICIOS E CORRETORA DE SEGUROS LTDA", "GENETICENTER - CENTRO DE GENETICA LTDA", "GERTH CONSULTORIA E PROMOCOES DE VENDAS LTDA", "GFF ENGENHARIA LTDA", "GIBRALTAR HOLDING LTDA", "GIOVANNI CARLECH GUIMARAES MARQUEZANI", "GMAC ESTACIONAMENTOS LTDA", "GMB ASSESSORIA LTDA", "GNV SETE BELO LTDA", "GPK PARTICIPACOES LTDA", "GR COMBUSTIVEIS LTDA", "GRB INDUSTRIA E COMERCIO DE EQUIPAMENTOS LTDA", "GRB INDUSTRIA E COMERCIO DE EQUIPAMENTOS LTDA FILIAL 03-50", "GRB INDUSTRIA E COMERCIO DE EQUIPAMENTOS LTDA FILIAL 04-31", "GRB INDUSTRIA E COMERCIO DE EQUIPAMENTOS LTDA FILIAL 05-12", "GROUND GESTAO PATRIMONIAL LTDA", "GSC GESTAO PATRIMONIAL LTDA", "GUIMARAES & VIEIRA DE MELLO SOCIEDADE DE ADVOGADOS", "GUIMARAES E VIEIRA DE MELLO ADVOGADOS", "GVM ADMINISTRACAO E CONSULTORIA LTDA", "GVM CONSORCIO", "GVM CORRETORA DE SEGUROS LTDA", "GWS ENGENHARIA LTDA", "GWS TECH LTDA", "H.C.-COMERCIO DE ALIMENTOS LTDA", "H.C.-COMERCIO DE ALIMENTOS LTDA", "HAND SHOP SUPRIMENTOS MEDICOS E TERAPEUTICOS LTDA", "HC COMERCIO DE ALIMENTOS LTDA", "HC COMERCIO DE ALIMENTOS LTDA FILIAL 03-63", "HOLDING MAIS MABC LTDA", "HOTEL SAO BENTO LTDA", "HPX PARTICIPACOES LTDA", "HSP GESTAO PATRIMONIAL LTDA", "HVAR INCORPORACOES LTDA", "I9 GESTAO E PARTICIPACOES LTDA", "IB COMBUSTIVEL LTDA", "IB TRANSPORTES & EMPREENDIMENTOS LTDA", "INCONFIDENTES PARTICIPACOES LTDA", "INCORPORADORA MONTE VERDE SPE LTDA", "INDUSTRIA DE TRANSFORMADORES KING LIMITADA", "INFLUXO SOCIEDADE DE PROFISSIONAIS", "INSTITUTO PERSONA INTELIGENCIA EMOCIONAL LTDA", "INTERWEG ADM E CORRETORA DE SEGUROS LTDA", "INTERWEG CORRETORA DE SEGUROS E BENEFICIOS LTDA", "J.V.V. GESTAO PATRIMONIAL LTDA", "JACL PARTICIPACOES LTDA", "JARDINO MALL LTDA", "JCA SERVICOS DE RADIOLOGIA LTDA", "JCM PARTICIPACOES LTDA", "JHCL GESTAO PATRIMONIAL LTDA", "JJA LOCACOES LTDA", "JKV GESTAO PATRIMONIAL LTDA", "JPAMACEDO E PARTICIPACOES LTDA", "JR LAVA JATO EIRELI", "JVC PARTICIPACOES LTDA", "JVP GESTAO PATRIMONIAL LTDA", "K10 PARTICIPACOES LTDA", "KALAB LOPES GESTAO PATRIMONIAL LTDA", "KALAB NEGOCIOS IMOBILIARIOS LTDA", "L.O. IMPORT EXPORT LTDA", "LABORATORIO DE PATOLOGIA CIRURGICA E CITOPATOLOGIA LTDA", "LABORATORIO DE PATOLOGIA CIRURGICA E CITOPATOLOGIA LTDA FILIAL 03-44", "LETOM EMPREENDIMENTOS LTDA", "LGX - PARTICIPACOES E ADMINISTRACAO LTDA", "LINK INDUSTRIA E COMERCIO DE MAQUINAS PARA MINERACAO LTDA", "LINK INDUSTRIA E COMERCIO DE MAQUINAS PARA MINERACAO LTDA FILIAL 03-05", "LOCS LOCADORA DE VEICULOS LTDA", "LS ENTERPRISE SOLLUTIONS LTDA", "M A B COSTA LTDA", "M L SILVEIRA SERVICOS CORPORATIVOS EIRELI", "MADA CLINICA ODONTOLOGICA LTDA", "MAIS CONSTRUCOES LTDA", "MAIS NEGOCIOS E REPRESENTACOES LTDA", "MAQUINAS RABELLO ITABAYANA LIMITADA", "MAR UP CONSULTORIA GESTAO E REPRESENTACAO COMERCIAL LTDA", "MAR9 TRATAMENTO DE DADOS LTDA", "MARCHALENTA AUTO SERVICOS LTDA", "MARCHALIVRE SERVICOS E PECAS LTDA", "MARCO GRILLI COMERCIO DE OBJETOS DE ARTE LTDA", "MARIA CHEQUER PARTICIPACOES LTDA", "MARIA CHEQUER PATRIMONIAL LTDA", "MARIANA CARLECH GUIMARAES MARQUEZANI", "MARICABI GESTAO PATRIMONIAL LTDA", "MASSIME DISTRIBUIDORA DE MEDICAMENTOS LTDA", "MASTER AUTO POSTO LTDA", "MASTER EMPREENDIMENTOS E PARTICIPACOES LTDA", "MASTER PISOS MATERIAL DE CONSTRUCAO EIRELI", "MATTA NUNES REPRESENTACOES COMERCIAIS E GESTAO DE NEGOCIOS LTDA", "MAX GESTAO PATRIMONIAL LTDA", "MD EMPREENDIMENTOS S.A", "MEDWAY SOLUCOES PARA A SAUDE LTDA", "MENDONCA E FERREIRA PARTICIPACOES LTDA", "MENDONCA E FERREIRA PATRIMONIAL LTDA", "MENDONCA E FILHOS GESTAO PATRIMONIAL LTDA", "MENDONCA PARTICIPACOES LTDA", "MEROS GESTAO PATRIMONIAL LTDA", "MG CONVENIENCIA LTDA", "MG CONVENIENCIA LTDA FILIAL 02-57", "MICRONIC COMERCIO E INDUSTRIA LTDA", "MILENE GUIMARAES MARQUEZANI", "MINAS GERAIS ADMINISTRADORA DE IMOVEIS LTDA", "MINEIRAO POSTO DE SERVICOS LTDA", "MLM HOLDING EIRELI", "MM COMERCIO DE DERIVADOS DE PETROLEO LTDA", "MMORAES PARTICIPACOES LTDA", "MONTE VERDE EDIFICACOES I SPE LTDA", "MONTE VERDE URBANIZACOES SPE LTDA", "MP INCORPORACOES LTDA", "MRI MOVIMENTACAO E RECUPERACAO INDUSTRIAL LTDA", "MRLIZ CONSULTORIA LTDA", "MTL PARTICIPACOES LTDA", "MULT SERVICOS ADMINISTRATIVOS LTDA", "MWA PARTICIPACOES LTDA", "MWA PATRIMONIAL LTDA", "NACIONAL RENOVAVEIS LTDA", "NATUREZA X COMERCIO LTDA", "NOSSA OBRA VAREJO DIGITAL LTDA", "NRSM REFORMAS LTDA", "NVB SERVICOS LTDA", "OLE PARTICIPACOES LTDA", "OLIVEIRA SANTOS ADVOGADOS", "OPEN-5 LTDA", "OPEN-5 LTDA", "OPX PARTICIPACOES LTDA", "ORGANIZACAO COMERCIAL MARINHO LTDA", "ORGANIZACOES SOUKI EIRELI", "ORGANIZACOES SOUKI EIRELI FILIAL 03-32", "ORIENT AUTOMOVEIS PECAS E SERVICOS LTDA", "ORIENT AUTOMOVEIS PECAS E SERVICOS LTDA FILIAL 03-43", "ORIENT AUTOMOVEIS PECAS E SERVICOS LTDA FILIAL 04-24", "ORIENTE FARMACEUTICA COMERCIO IMPORTACAO E EXPORTACAO LTDA", "PADUA COMERCIO E INDUSTRIA LTDA", "PAIVA BRANT LTDA", "PAIVA EMPREENDIMENTOS E GESTAO DE IMOVEIS PROPRIOS LTDA", "PCFORYOU LTDA", "PEMAX INTERMEDIACAO E NEGOCIOS LTDA", "PERFORMANCE GESTAO EMPRESARIAL LTDA", "PETRODATA PROCESSAMENTO DE DADOS LTDA", "PLATAFORMA AM3 LTDA", "PNEUS JUA COMERCIO DE PNEUS LTDA", "PONTUAUTO CENTRO AUTOMOTIVO LTDA", "POP EMPREENDIMENTOS E PARTICIPACOES S/A", "POSTO AEROPORTO LTDA", "POSTO AGUIA COMERCIO DE COMBUSTIVEIS LTDA", "POSTO ALAMO LTDA", "POSTO ALLGAS LTDA", "POSTO AVENIDA BRASIL COMERCIO DE COMBUSTIVEIS LTDA", "POSTO BALNEARIO AGUA LIMPA LTDA", "POSTO BARAO VPP LTDA", "POSTO BERIMBAU LTDA", "POSTO BURITIS LTDA", "POSTO CATEDRAL LTDA", "POSTO CENTER NORTE LTDA", "POSTO COELHO LTDA", "POSTO DANUBIO LTDA", "POSTO DE COMBUSTIVEIS CENTER SUL LTDA", "POSTO DE COMBUSTIVEIS SANTO AGOSTINHO LTDA", "POSTO DE COMBUSTIVEL PETROLANDIA LTDA", "POSTO DE COMBUSTIVEL VILA CRUZEIRO LIMITADA", "POSTO ESTORIL LTDA", "POSTO FORMULA BR LTDA", "POSTO HUGO WERNECK LTDA", "POSTO IPE COMERCIO DE COMBUSTIVEIS LTDA", "POSTO IRMAOS AULER LTDA", "POSTO JUPITER LTDA", "POSTO LESTE LTDA", "POSTO MARIO WERNECK LIMITADA", "POSTO MAURITANIA LTDA", "POSTO MINAS SHOPPING LTDA", "POSTO MINASLANDIA LTDA", "POSTO MONTE VERDE LTDA", "POSTO MUSTANG LTDA", "POSTO NOGUEIRINHA LTDA", "POSTO OCEANO AZUL LTDA", "POSTO OCEANO LTDA", "POSTO PANAMERA LTDA", "POSTO PARQUE BURITIS LTDA", "POSTO PARQUE JARDIM LTDA", "POSTO PICA PAU LTDA", "POSTO POETA LTDA", "POSTO PORTAL DE BETIM LTDA", "POSTO PORTAL DE CONTAGEM LTDA", "POSTO PORTAL DOS CAICARAS LTDA", "POSTO SIGMA LTDA", "POSTO SOBERANO AUTORAMA LTDA", "POSTO SOBERANO KARRAO LTDA", "POSTO SOBERANO SETE DE SETEMBRO LTDA", "POSTO TATIANA LTDA", "POSTO TROVAO LTDA", "POSTO VIA FERNAO DIAS LTDA", "POSTO VILA CHALE LTDA", "POSTO VILA DA SERRA LTDA", "POSTO VILA PICA PAU LTDA", "POSTO ZEPPE GRAND PRIX LTDA", "POSTO ZEPPE MG LTDA", "POSTO ZEPPE OASIS LTDA", "POSTO ZEPPE SAO JOSE LTDA", "POSTO ZEPPELIN LTDA", "PPML INDUSTRIA E COMERCIO DE ROUPAS EIRELI", "PRESERVAR PARTICIPACOES LTDA", "PRIMA LINEA AUTOMOVEIS LTDA", "PRIMOLA FRAGRANCIAS LTDA FILIAL 04-30", "PROFIT FOODS LTDA", "PROJETOUM COMERCIO E REPRESENTACOES LTDA", "PROJETOUM COMERCIO E REPRESENTACOES LTDA FILIAL 0002-27", "PROPELLER LTDA", "PROSERVICE LTDA", "PROSPECTIVA SOCIEDADE DE PROFISSIONAIS", "PURA SAUDE ALIMENTOS LTDA", "PURA SAUDE ALIMENTOS LTDA FILIAL 02-88", "QUADRIJET ALPHAVILLE COMERCIO LTDA", "QUEOPZ GESTAO PATRIMONIAL LTDA", "QUIBASA QUIMICA BASICA LTDA", "QUIBASA QUIMICA BASICA LTDA FILIAL 02-98", "QUIBASA QUIMICA BASICA LTDA FILIAL 03-79", "QUICK CONVENIENCIAS LTDA", "QUICK LUBE COMERCIO DE PRODUTOS E FRANQUIAS LTDA", "RACCO EQUIPAMENTOS E SERVICOS EIRELI", "RACCO SERVICOS DE PUBLICIDADE E COMUNICACAO LTDA", "RC INVEST PARTICIPACOES LTDA", "RECICLAGEM PASSARELA LTDA", "REDE A PUBLICIDADE E PROPAGANDA LTDA", "REDE OFFICE INCORPORACOES LTDA", "RESIDENCIAL ANDORINHAS SPE LTDA", "RESIDENCIAL PACIFICO RIBEIRAO DAS NEVES SPE LTDA", "RESIDENCIAL PACIFICO RIBEIRAO DAS NEVES SPE LTDA FILIAL 02-72", "RESIDENCIAL VILA AMAZONAS SPE LTDA","RESIDENCIAL VILA AMAZONAS SPE LTDA FILIAL 02-91", "RESIDENCIAL VILA ATLANTICO SABARA SPE LTDA", "RESIDENCIAL VILA ATLANTICO SABARA SPE LTDA", "RESIDENCIAL VILA CONCEICAO SPE LTDA", "RESIDENCIAL VILA CONCEICAO SPE LTDA FILIAL 02-01", "RESIDENCIAL VILA MORGANTI I SCP", "RESIDENCIAL VILA MORGANTI I SPE LTDA", "RESIDENCIAL VILA MORGANTI I SPE LTDA FILIAL 02-05", "RESIDENCIAL VILA SAO JOSE I SPE LTDA", "RESIDENCIAL VILA SAO JOSE I SPE LTDA FILIAL 02-64", "RESIDENCIAL VILA SAO JOSE II SPE LTDA", "RESIDENCIAL VILA SAO JOSE II SPE LTDA FILIAL 0002-01", "RESIDENCIAL VILA SAO JOSE SCP", "RETES IMAGENS SERVICOS E CONSULTORIA LTDA", "RFX ADMINISTRACAO DE RECURSOS LTDA", "RFX CONSULTORIA E GESTAO DE NEGOCIOS LTDA", "RFX DISTRIBUIDORA DE PRODUTOS AUTOMOTIVOS LTDA", "RFX GESTAO PATRIMONIAL LTDA", "RFX LOGISTICA E TRANSPORTES DE COMBUSTIVEIS LTDA", "RFX TREINAMENTO PROFISSIONAL LTDA", "RGGC EMPREENDIMENTOS LTDA", "RH CENTRO DE SAUDE LTDA", "RICARDO SANTOS BRANT", "ROCKET GESTAO PATRIMONIAL LTDA", "ROL COMERCIO DE DERIVADOS DE PETROLEO LTDA", "RPB COMERCIO DE COMBUSTIVEL LTDA", "RSM COMERCIO E GERENCIAMENTO DE RESIDUOS GUAXUPE EIRELI", "SAINT EMILION AUTOMOVEIS PECAS E SERVICOS LTDA", "SAINT EMILION AUTOMOVEIS PECAS E SERVICOS LTDA", "SAINT EMILION AUTOMOVEIS PECAS E SERVICOS LTDA", "SAINT EMILION AUTOMOVEIS PECAS E SERVICOS LTDA", "SANTA CLARA AGROPECUARIA LTDA", "SANTA MARIA ECOLOGIC EQUIPAMENTOS LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC LTDA", "SANTA MARIA ECOLOGIC RESIDUOS LTDA", "SANTORINI POSTO DE SERVICOS LTDA", "SARAMENHA ENGENHARIA LTDA", "SCP AUDITORIA DE IMPOSTOS E CONTRIBUICOES", "SCP CLAM ENGENHARIA LTDA", "SCP CLINICA RADIOLOGICA ELDORADO LTDA", "SCP DIAGNOSTICO BETIMBARREIRO LTDA", "SCP RESIDENCIAL VILA CONCEICAO", "SCP VILA PACIFICO SANCRUZA", "SE LOTEAMENTOS LTDA", "SETEC- CONSULTORIA EMPRESARIAL LTDA", "SICAL INDUSTRIAL LTDA", "SIMEX ENTREGAS E MOVIMENTACAO DE CARGAS LTDA", "SIX TRACKS LTDA", "SOBERANO LOJAS DE CONVENIENCIA LTDA", "SOBERANO LUBRIFICANTES LTDA", "SOBERANO SERVICOS LTDA", "SOBERANO TRANSPORTES LTDA", "SOLAR VOLT SOLUCOES COMERCIO E INSTALACAO PARA ENERGIA LTDA", "SOLUCAO CORTE E DOBRA DE METAIS LTDA", "SOLVE OPERACAO, MANUTENCAO E COMISSIONAMENTO DE SISTEMAS FOTOVOLTAICOS LTDA", "SOLVIA SOLUCOES VIARIAS LTDA", "SP IMPORTS LTDA", "SP IMPORTS LTDA FILIAL 02-70", "SP IMPORTS LTDA FILIAL 03-50", "SPE JARDINS DOS BURITIS LTDA", "SPE JARDINS DOS BURITIS LTDA FILIAL 02-60", "SPE LA BRESSE LTDA", "SPE MARIA FAUSTINA LTDA", "SPE MIRANTE DO LAGO SETE LAGOAS LTDA", "SSME EMPREENDIMENTOS IMOBILIARIOS LTDA FILIAL 02-76", "SSME EMPREENDIMENTOS IMOBILIARIOS LTDA", "SSME FLORESTAL LTDA", "SSME FLORESTAL LTDA FILIAL 0002-43", "SSME FLORESTAL LTDA FILIAL 0003-24", "SSME FLORESTAL LTDA FILIAL 0005-96", "SSME FLORESTAL LTDA FILIAL 0006-77", "SSME FLORESTAL LTDA FILIAL 0007-58", "SSME FLORESTAL LTDA FILIAL 0008-39", "SSME FLORESTAL LTDA FILIAL 0009-10", "SSME FLORESTAL LTDA FILIAL 0010-53", "SSME FLORESTAL LTDA FILIAL 0011-34", "SSME FLORESTAL LTDA FILIAL 0012-15", "SSME FLORESTAL LTDA FILIAL 0013-04", "SSME FLORESTAL LTDA FILIAL 0014-87", "SUDESTE ADMINISTRADORA DE SERVICOS LTDA", "SUDESTE ENGENHARIA E COMERCIO LTDA", "SUDESTE ENGENHARIA E COMERCIO LTDA FILIAL 02-39", "SUDESTE ENGENHARIA E COMERCIO LTDA FILIAL 03-10", "SUDESTE PARTICIPACOES LTDA", "SV LOGISTICA LTDA", "SV RANCHO VELHO GERACAO DE ENERGIA SPE LTDA", "SWA PARTICIPACOES LTDA", "SWA PATRIMONIAL LTDA", "TAKONO DISTRIBUICAO LTDA", "TASK SOFTWARE LTDA", "TAX CLOUD SOLUCOES LTDA", "TCX COMERCIO E INDUSTRIA DE EQUIPAMENTOS PECAS E SERVICOS LTDA", "TEBAS ADMINISTRACAO LTDA", "TECHNEACO ENGENHARIA LTDA", "TECHNEACO ENGENHARIA LTDA FILIAL 02-58", "TECNOCAP RECAPAGEM E PNEUS LTDA", "THAISSA CALAB CURSOS LTDA", "THAISSA CALAB ODONTOLOGIA LTDA", "TIMBIRAS PARTICIPACOES LTDA", "TK LOCACAO DE EQUIPAMENTOS LTDA", "TK PATRIMONIAL LTDA", "TLUANER PARTICIPACOES S/A", "TMJ MARCA E PATENTE LTDA", "TOP RAJA CAR LOCADORA DE VEICULOS LTDA", "TOPAZIO IMPERIAL MINERACAO COMERCIO E INDUSTRIA LTDA", "TRANSPORTADORA DONIZETE LTDA", "TRANSPORTES BOA VISTA LOGISTICA LTDA", "TRIACO ESTRUTURAS METALICAS LTDA", "TURMALINA INCORPORACOES SPE LTDA", "USA DIAGNOSTICA LTDA", "VALADAO E SANTOS PARTICIPACOES LTDA", "VALUMA COBRANCA E NEGOCIOS LTDA", "VCA COMERCIO LTDA", "VCS COMERCIO LTDA", "VEIGA ESTRUTURAS METALICAS LTDA", "VENETO EMPREENDIMENTO COMERCIAL LTDA", "VEREDAS DA SERRA COMBUSTIVEL LTDA", "VERO LATTE COMERCIO DE ALIMENTOS LTDA", "VERO LATTE COMERCIO DE ALIMENTOS LTDA", "VERO LATTE COMERCIO DE ALIMENTOS LTDA", "VIA MONDO APS LTDA", "VIA MONDO APS LTDA", "VIA MONDO AUTOMOVEIS E PECAS LTDA", "VIA MONDO AUTOMOVEIS E PECAS LTDA", "VIA MONDO AUTOMOVEIS E PECAS LTDA", "VIA MONDO AUTOMOVEIS E PECAS LTDA", "VIA MONDO AUTOMOVEIS E PECAS LTDA", "VIA MONDO AUTOMOVEIS E PECAS LTDA", "VIA MONDO AUTOMOVEIS E PECAS LTDA - FILIAL 08-80", "VIA MONDO AUTOMOVEIS E PECAS LTDA - FILIAL 09-61", "VIA MONDO DISTRIBUIDORA DE PECAS E ACESSORIOS AUTOMOTIVOS LTDA",  "VIA MONDO DISTRIBUIDORA DE PECAS E ACESSORIOS AUTOMOTIVOS LTDA", "VIA MONDO FANDI LTDA", "VIA MONDO LOCADORA LTDA", "VIA MONDO LOCADORA LTDA FILIAL 02-94", "VIA MONDO LOCADORA LTDA FILIAL 03-75", "VIA MONDO MULTIMARCAS LTDA", "VIA MONDO TRANSPORTES LTDA", "VIEIRA ADMINISTRACAO LTDA", "VILA CLARA VITORIA LTDA", "VJ PARTICIPACOES LTDA", "VJ PATRIMONIAL LTDA", "VN EMPREENDIMENTOS LTDA", "VSX VALVULAS E EQUIPAMENTOS LTDA", "WOLF PARTICIPACOES S/A", "WRN PARTICIPACOES LTDA", "ZOX GESTAO PATRIMONIAL LTDA"]

# Lista de funcionalidades disponíveis
lista_funcionalidades = ["Página Inicial" , "Chat" , "Organizar Arquivos Fiscais", "Controle Importação", "Registros Importação", "Indicadores", "Configurações"]


# Verificar se as colunas 'empresas' e 'permissoes' existem e adicioná-las se necessário
cursor.execute("PRAGMA table_info(users)")
columns = [col[1] for col in cursor.fetchall()]
if "empresas" not in columns:
    cursor.execute("ALTER TABLE users ADD COLUMN empresas TEXT DEFAULT ''")
if "permissoes" not in columns:
    cursor.execute("ALTER TABLE users ADD COLUMN permissoes TEXT DEFAULT ''")
conn.commit()

# Função para hashear senha
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Adicionar usuário administrador
cursor.execute("INSERT OR REPLACE INTO users (username, password, empresas, permissoes) VALUES (?, ?, ?, ?)", 
               ("USUARIO", hash_password("Refinnehj262"), ",".join(lista_empresas), ",".join(lista_funcionalidades)))
conn.commit()

# Função para adicionar ou atualizar usuário
def save_user(username, password, empresas, permissoes):
    hashed_password = hash_password(password) if password else None
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    user_exists = cursor.fetchone()
    
    if user_exists:
        if password:
            cursor.execute("UPDATE users SET password = ?, empresas = ?, permissoes = ? WHERE username = ?", 
                           (hashed_password, empresas, permissoes, username))
        else:
            cursor.execute("UPDATE users SET empresas = ?, permissoes = ? WHERE username = ?", 
                           (empresas, permissoes, username))
    else:
        cursor.execute("INSERT INTO users (username, password, empresas, permissoes) VALUES (?, ?, ?, ?)", 
                       (username, hashed_password, empresas, permissoes))
    conn.commit()
    return True

# Função para excluir usuário
def delete_user(username):
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()

# Função para validar login
def validate_login(username, password):
    cursor.execute("SELECT password, empresas, permissoes FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    if user_data and user_data[0] == hash_password(password):
        st.session_state.empresas = user_data[1].split(",") if user_data[1] else []
        st.session_state.permissoes = user_data[2].split(",") if user_data[2] else []
        return True
    return False

# Tela de Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if validate_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos!")
    st.stop()

# Menu restrito conforme permissões do usuário
menu_options = [option for option in lista_funcionalidades if option in st.session_state.permissoes]
menu = st.sidebar.selectbox("Escolha a funcionalidade", menu_options)



if menu == "Configurações":
    st.title("Configurações - Gerenciamento de Usuários")
    
    with st.form("add_user_form"):
        new_username = st.text_input("Usuário")
        new_password = st.text_input("Senha (deixe em branco para não alterar)", type="password")
        empresas_selecionadas = st.multiselect("Empresas associadas", lista_empresas)
        permissoes_selecionadas = st.multiselect("Funcionalidades permitidas", lista_funcionalidades)
        empresas_str = ",".join(empresas_selecionadas)
        permissoes_str = ",".join(permissoes_selecionadas)
        save_button = st.form_submit_button("Salvar Usuário")
        
        if save_button and new_username:
            if save_user(new_username, new_password, empresas_str, permissoes_str):
                st.success("Usuário salvo com sucesso!")
                st.rerun()
            else:
                st.error("Erro ao salvar usuário!")
    
    st.subheader("Usuários Cadastrados")
    cursor.execute("SELECT username, empresas, permissoes FROM users")
    users = cursor.fetchall()
    for user in users:
        st.write(f"Usuário: {user[0]} | Empresas: {user[1]} | Permissões: {user[2]}")
        if st.button(f"Remover {user[0]}", key=f"del_{user[0]}"):
            delete_user(user[0])
            st.rerun()



# Conectar ao banco de dados
conn = sqlite3.connect("importacao02_register.db", check_same_thread=False)
cursor = conn.cursor()

#Organizador de Arquivos Fiscais
def salvar_arquivo(arquivo, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_completo = os.path.join(pasta_destino, arquivo.name)
    with open(caminho_completo, "wb") as f:
        f.write(arquivo.getbuffer())
def extrair_zip(arquivo_zip, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)
    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)
def verificar_arquivo(arquivo):
    try:
        if arquivo.name.endswith(".xml") or arquivo.name.endswith(".txt"):
            conteudo = arquivo.read()
            if not conteudo.strip():
                return False
        return True
    except Exception as e:
        return False
def classificar_arquivo(nome_arquivo):
    categorias = {
        "NFE": ["NFe", "entrada", "saída"],
        "CTE_ENTRADA": ["CTe", "entrada"],
        "CTE_SAIDA": ["CTe", "saida"],
        "CTE_CANCELADA": ["CTe", "cancelada"],
        "NFCE_SAIDA": ["NFCe"],
        "SPED": ["SPED", ".txt"],
        "NFS_TOMADOS": [ "nfse"],
        "NFS_PRESTADO": ["nfse"],
        "PLANILHA": [".xls", ".xlsx", "csv"],
    }
    nome_arquivo_lower = nome_arquivo.lower()
    for categoria, palavras_chave in categorias.items():
        if any(palavra.lower() in nome_arquivo_lower for palavra in palavras_chave):
            return categoria
    return "OUTROS"
def processar_arquivos(uploaded_files, nome_empresa):
    if not nome_empresa:
        st.error("Por favor, digite o nome da empresa antes de processar os arquivos.")
        return
    
    with tempfile.TemporaryDirectory() as pasta_temp:
        pasta_empresa = os.path.join(pasta_temp, nome_empresa)
        os.makedirs(pasta_empresa, exist_ok=True)
        arquivos_corrompidos = []
        
        for arquivo in uploaded_files:
            if not verificar_arquivo(arquivo):
                arquivos_corrompidos.append(arquivo.name)
                continue
            
            if arquivo.name.endswith(".zip"):
                pasta_extracao = os.path.join(pasta_empresa, "TEMP_ZIP")
                os.makedirs(pasta_extracao, exist_ok=True)
                
                with open(os.path.join(pasta_extracao, arquivo.name), "wb") as f:
                    f.write(arquivo.getbuffer())
                
                extrair_zip(os.path.join(pasta_extracao, arquivo.name), pasta_extracao)
                
                for raiz, _, arquivos in os.walk(pasta_extracao):
                    for nome_arquivo in arquivos:
                        caminho_arquivo = os.path.join(raiz, nome_arquivo)
                        categoria = classificar_arquivo(nome_arquivo)
                        pasta_destino = os.path.join(pasta_empresa, categoria)
                        os.makedirs(pasta_destino, exist_ok=True)
                        shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
                
                shutil.rmtree(pasta_extracao)
            else:
                categoria = classificar_arquivo(arquivo.name)
                pasta_destino = os.path.join(pasta_empresa, categoria)
                salvar_arquivo(arquivo, pasta_destino)
        
        if arquivos_corrompidos:
            st.warning(f"Os seguintes arquivos estão corrompidos e não foram processados: {', '.join(arquivos_corrompidos)}")
        
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            for raiz, _, arquivos in os.walk(pasta_empresa):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo)
                    zipf.write(caminho_completo, os.path.relpath(caminho_completo, pasta_empresa))
        zip_buffer.seek(0)
        
        st.success("Arquivos processados com sucesso! Faça o download abaixo.")
        st.download_button("Baixar Arquivos Processados", zip_buffer, f"{nome_empresa}.zip", "application/zip")
        


if menu == "Organizar Arquivos Fiscais":
    st.title("Organizador de Arquivos Fiscais")
    nome_empresa = st.selectbox("Nome da Empresa", st.session_state.empresas)

    uploaded_files = st.file_uploader("Envie seus arquivos XML, TXT, ZIP ou Excel", accept_multiple_files=True)



if menu == "Organizar Arquivos Fiscais": 
    if st.button("Processar Arquivos"):
        zip_buffer = processar_arquivos(uploaded_files, nome_empresa)
        if zip_buffer:
            st.success("Arquivos processados com sucesso! Faça o download abaixo.")
            st.download_button(
                "Baixar Arquivos Processados", 
                zip_buffer, 
                f"{nome_empresa}.zip", 
                "application/zip"
            )





elif menu == "Controle Importação":
    st.title("📑 Importação")
    with st.form("registro_form"):
        empresa_filtro = st.selectbox("Nome da empresa", st.session_state.empresas)

        tipo_nota = st.selectbox("Tipo de Nota", ["NFE entrada", "NFE saída", "CTE entrada", "CTE saída", "CTE cancelado", "SPED", "NFS tomado", "NFS prestado", "Planilha", "NFCE saída"])
        erro = st.text_area("Erro (se houver)")
        arquivo = st.file_uploader("Anexar imagem do erro", type=["png", "jpeg", "jpg"])
        submit = st.form_submit_button("Registrar")
        if submit:
            data_atual = date.today().strftime("%d-%m-%Y")
            arquivo_path = ""
            
            if arquivo:
                pasta_arquivos = "arquivos_erros"
                os.makedirs(pasta_arquivos, exist_ok=True)
                arquivo_path = os.path.join(pasta_arquivos, f"{data_atual}_{arquivo.name}")
                with open(arquivo_path, "wb") as f:
                    f.write(arquivo.read())
            
            status = 'OK' if not erro else 'Pendente'
            cursor.execute("""
                                CREATE TABLE IF NOT EXISTS registros (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                data TEXT,
                                empresa TEXT,
                                tipo_nota TEXT,
                                erro TEXT,
                                arquivo_erro TEXT,
                                status TEXT)""")
            conn.commit()

            cursor.execute("INSERT INTO registros (data, empresa, tipo_nota, erro, arquivo_erro, status) VALUES (?, ?, ?, ?, ?, ?)",
                        (data_atual, empresa_filtro, tipo_nota, erro, arquivo_path, status))
            conn.commit()
            st.success("✅ Registro salvo com sucesso!")
        


# Função para abrir o Outlook com uma nova mensagem
def open_outlook(email_destino, assunto, corpo, arquivo_erro=None):
    try:
        # Codifica os parâmetros do e-mail para evitar problemas com caracteres especiais
        assunto = urllib.parse.quote(assunto)
        corpo = urllib.parse.quote(corpo)

        # Se o arquivo de erro existir, adicione ao corpo do e-mail (será necessário adicionar manualmente como anexo no Outlook)
        if arquivo_erro and os.path.exists(arquivo_erro):
            corpo += f"\n\nAnexo: {arquivo_erro}"  # Aqui, o link para o arquivo será incluído no corpo

        # Monta o comando mailto para abrir a tela de envio de e-mail no Outlook
        mailto_link = f"mailto:{email_destino}?subject={assunto}&body={corpo}"
        
        # Usa o webbrowser para abrir o link "mailto" diretamente
        webbrowser.open(mailto_link)
    except Exception as e:
        st.error(f"Erro ao tentar abrir o Outlook: {str(e)}")

# Inicializa o estado de envio de e-mail
if "emails_enviados" not in st.session_state:
    st.session_state["emails_enviados"] = {}

# Seu código com a parte do menu
if menu == "Registros Importação":
    st.title("🔍 Buscar Registros")

    # Verifica se o usuário tem permissão para acessar registros
    if not st.session_state.empresas:
        st.warning("⚠ Você não tem permissão para acessar registros de nenhuma empresa.")
        st.stop()

    empresa_filtro = st.selectbox("Nome da empresa", st.session_state.empresas)

    # Conectando ao banco de dados SQLite
    conn = sqlite3.connect('importacao02_register.db')
    cursor = conn.cursor()

    query = "SELECT * FROM registros"
    if empresa_filtro:
        query += " WHERE empresa LIKE ?"
        registros = pd.read_sql_query(query, conn, params=(f"%{empresa_filtro}%",))
    else:
        registros = pd.read_sql_query(query, conn)

    st.subheader("📋 Registros Importação")
    if not registros.empty:
        for index, row in registros.iterrows():
            with st.expander(f"📌 {row['empresa']} - {row['tipo_nota']}"):
                st.write(f"**Erro:** {row['erro']}" if row['erro'] else "**Sem erro registrado.**")
                st.write(f"**Data:** {row['data']}")
                st.write(f"**Status:** {row['status']}")

                # Exibindo a imagem do arquivo de erro
                if row['arquivo_erro'] and os.path.exists(row['arquivo_erro']):
                    st.markdown(f"[📷 Visualizar Imagem]({row['arquivo_erro']})", unsafe_allow_html=True)
                    st.image(row['arquivo_erro'], caption="Imagem do erro", use_container_width=True)

                # Se houver um erro, permitir o envio do e-mail
                if row['erro']:
                    # Campo para o usuário digitar o e-mail do cliente
                    email_cliente = st.text_input(f"Digite o e-mail do cliente para {row['empresa']}", key=f"email_{row['id']}")

                    erro_mensagem = f"Ocorreu um erro na importação do arquivo. Detalhes: {row['erro']}"
                    assunto = f"Erro na Importação de Arquivo - {row['empresa']}"

                    # Verifica se o e-mail já foi enviado para evitar aberturas repetidas
                    if email_cliente and st.button(f"🔔 Abrir e-mail para {email_cliente}", key=f"abrir_email_{row['id']}"):
                        # Passa o arquivo de erro, se disponível, para ser mencionado no corpo
                        open_outlook(email_cliente, assunto, erro_mensagem, row['arquivo_erro'])
                        st.success(f"📧 E-mail pronto para envio no Outlook! O anexo precisa ser adicionado manualmente.")

                # Botão para marcar como "Resolvido"
                if row['status'] == "Pendente":
                    if st.button("✔ OK", key=f"resolver_{row['id']}"):
                        cursor.execute("UPDATE registros SET status = 'Resolvido' WHERE id = ?", (row['id'],))
                        conn.commit()
                        st.success(f"✅ Status do registro {row['id']} atualizado para 'Resolvido'.")
                        st.rerun()

    conn.close()


elif menu == "Indicadores":
    st.title("📈 Indicadores de Importação")
    if not st.session_state.empresas:
        st.warning("⚠ Você não tem permissão para acessar indicadores de nenhuma empresa.")
        st.stop()

    query = "SELECT * FROM registros WHERE empresa IN ({})".format(",".join(["?"] * len(st.session_state.empresas)))
    registros = pd.read_sql_query(query, conn, params=st.session_state.empresas)

    
    if not registros.empty:
        col1, col2 = st.columns(2)
        empresa_count = registros["empresa"].value_counts().reset_index()
        empresa_count.columns = ["Empresa", "Total de Registros"]
        fig1 = px.pie(empresa_count, names="Empresa", values="Total de Registros", title="📌 Registros por Empresa")
        col1.plotly_chart(fig1)
        
        tipo_nota_count = registros["tipo_nota"].value_counts().reset_index()
        tipo_nota_count.columns = ["Tipo de Nota", "Quantidade"]
        fig2 = px.pie(tipo_nota_count, names="Tipo de Nota", values="Quantidade", title="📌 Tipos de Nota Registradas")
        col2.plotly_chart(fig2)
        
        importadas = registros["empresa"].nunique()
        total_registros = len(registros)
        df_empresas = pd.DataFrame({"Status": ["Importadas", "Não Importadas"], "Quantidade": [importadas, total_registros - importadas]})
        fig3 = px.pie(df_empresas, names="Status", values="Quantidade", title="📌 Empresas Importadas vs. Não Importadas")
        st.plotly_chart(fig3)
        
        if registros["erro"].notna().sum() > 0:
            erro_count = registros["erro"].value_counts().reset_index().head(5)
            erro_count.columns = ["Erro", "Frequência"]
            st.subheader("🔴 Erros Mais Comuns")
            fig4 = px.pie(erro_count, names="Erro", values="Frequência", title="📌 Erros Mais Frequentes")
            st.plotly_chart(fig4)
    
    st.subheader("📥 Download de Registros")
    data_hoje = date.today().strftime("%d-%m-%Y")
    df_hoje = registros[registros['data'] == data_hoje]
    if not df_hoje.empty:
        csv = df_hoje.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Baixar Planilha do Dia", data=csv, file_name=f"registros_{data_hoje}.csv", mime="text/csv")
    else:
        st.info("Nenhum registro encontrado para hoje.")



# Função para carregar as mensagens salvas
def load_messages():
    if os.path.exists("messages.txt"):
        with open("messages.txt", "r") as f:
            return f.readlines()
    else:
        return []

# Função para salvar as mensagens
def save_message(username, message):
    # Pega o horário atual no formato HH:MM:SS
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("messages.txt", "a") as f:
        f.write(f"{timestamp} - {username}: {message}\n")

# Função para pegar o nome do usuário a partir do banco de dados
def get_user_name():
    # Conectar ao banco de dados
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Selecionar o primeiro usuário ou um usuário específico
    cursor.execute("SELECT username FROM users LIMIT 1")
    user = cursor.fetchone()

    conn.close()

    # Retornar o nome do usuário ou um padrão
    if user:
        return user[0]
    else:
        return "Usuário desconhecido"

# Função para exibir o chat
if menu == "Chat":
    st.title("Chat Entre Usuários")

    # Pegar o nome do usuário do banco de dados
    username = get_user_name()

    # Carregar mensagens antigas
    messages = load_messages()

    input_area = st.container()  # Área fixa para digitar a mensagem
    # Fixa a caixa de entrada na parte inferior da tela
    with input_area:
        user_message = st.text_input("Digite sua mensagem:")

    # Enviar a mensagem
    if st.button("Enviar"):
        if user_message:
            # Salvar a mensagem com o nome do usuário e hora
            save_message(username, user_message)
            st.text(f"Você ({username}): {user_message}")
            st.rerun()  # Atualiza a página (não é mais necessário com a abordagem abaixo)   
    chat_area = st.container()  # Área para exibir as mensagens


    # Exibir as mensagens antigas
    with chat_area:
        st.write("### Mensagens:")
        for msg in messages:
            st.text(msg)





# Função para exibir a página inicial
if menu == "Página Inicial":
    st.title("Bem Vindo")
    st.write("Assista o tutorial de como utilizar nosso sistema.")
    # URL do vídeo que será exibido na página inicial
    video_url = "https://youtu.be/aP0sPUVjs40?si=n_lO5UnNNKR1mBwe"  # Substitua pelo link do seu vídeo

    # Exibe o vídeo diretamente na página inicial
    st.video(video_url)


