-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: biblioteca
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `livros`
--

DROP TABLE IF EXISTS `livros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_livro` varchar(45) NOT NULL,
  `tipo` varchar(45) DEFAULT NULL,
  `cod_livro` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livros`
--

LOCK TABLES `livros` WRITE;
/*!40000 ALTER TABLE `livros` DISABLE KEYS */;
INSERT INTO `livros` VALUES (1,'Don Quixote','','10000'),(2,'Um Conto de Duas Cidades','','10001'),(3,'O Senhor dos Anéis','','10002'),(4,'O Pequeno Príncipe','','10003'),(5,'Harry Potter e a Pedra Filosofal','','10004'),(6,'O Hobbit','','10005'),(7,'O Caso dos Dez Negrinhos [nota 1]','','10006'),(8,'O Sonho da Câmara Vermelha','','10007'),(9,'Ela  a Feiticeira','','10008'),(10,'O Leão a Feiticeira e o Guarda-Roupa','','10009'),(11,'O Código Da Vinci','','10010'),(12,'Pense e Enriqueça','','10011'),(13,'O Alquimista','','10012'),(14,'Harry Potter e o Enigma do Príncipe','','10013'),(15,'O Apanhador no Campo de Centeio [nota 2]','','10014'),(16,'Harry Potter e a Câmara Secreta','','10015'),(17,'Harry Potter e o Prisioneiro de Azkaban','','10016'),(18,'Harry Potter e o Cálice de Fogo','','10017'),(19,'Harry Potter e a Ordem da Fênix','','10018'),(20,'Harry Potter e as Relíquias da Morte','','10019'),(21,'Cem Anos de Solidão','','10020'),(22,'Lolita','','10021'),(23,'Heidi','','10022'),(24,'Meu Filho Meu Tesouro','','10023'),(25,'Anne of Green Gables [nota 3]','','10024'),(26,'Beleza Negra [nota 4]','','10025'),(27,'O Nome da Rosa','','10026'),(28,'A Águia Pousou','','10027'),(29,'Era uma Vez em Watership Down','','10028'),(30,'O Relatório Hite sobre sexualidade feminina','','10029'),(31,'A Menina e o Porquinho [nota 5]','','10030'),(32,'Um Safado em Dublin','','10031'),(33,'As Pontes de Madison','','10032'),(34,'Ben-Hur: Uma História dos Tempos de Cristo','','10033'),(35,'[nota 6] The Mark of Zorro','','10034'),(36,'A História do Pedro Coelho','','10035'),(37,'Fernão Capelo Gaivota','','10036'),(38,'Cinquenta Tons de Cinza [nota 7]','','10037'),(39,'Mensagem a Garcia','','10038'),(40,'O Mundo de Sofia','','10039'),(41,'O Jardim dos Esquecidos','','10040'),(42,'Anjos e Demônios','','10041'),(44,'Voyna i mir  Guerra e Paz','','10043'),(45,'As Aventuras de Pinóquio','','10044'),(46,'Você pode curar sua vida','','10045'),(47,'Seus Pontos Fracos','','10046'),(48,'O Falecido Grande Planeta Terra','','10047'),(49,'Caim e Abel','','10048'),(50,'Pássaros Feridos','','10049'),(51,'O Vale das Bonecas','','10050'),(52,'Em Seus Passos o Que Faria Jesus?','','10051'),(53,'O Sol é Para Todos [nota 8]','','10052'),(54,'O Símbolo Perdido','','10053'),(55,'...E o Vento Levou [nota 9]','','10054'),(56,'Diário de Anne Frank','','10055'),(57,'Uma Vida com Propósitos','','10056'),(58,'The Revolt of Mamie Stover','','10057'),(60,'Uma Lagarta Muito Comilona','','10059'),(61,'A Jovem Guarda','','10060'),(62,'Quem Mexeu no Meu Queijo?','','10061'),(63,'O Grande Gatsby','','10062'),(64,'O Vento nos Salgueiros','','10063'),(65,'Mil Novecentos e Oitenta e Quatro','','10064'),(67,'Podnyataya Tselina  Virgin Soil Upturned','','10066'),(68,'A Profecia Celestina','','10067'),(69,'Jogos Vorazes [nota 11]','','10068'),(70,'Dyadya Styopa  Tio Styopa','','10069'),(71,'O Poderoso Chefão [nota 12]','','10070'),(72,'Uma História de Amor','','10071'),(73,'O Totem do Lobo','','10072'),(74,'A Aliciadora Feliz','','10073'),(75,'Tubarão','','10074'),(76,'Love You Forever','','10075'),(77,'The Women\'s Room','','10076'),(78,'O Que Esperar Quando Você Está Esperando','','10077'),(79,'As Aventuras de Huckleberry Finn','','10078'),(80,'O diário secreto de um adolescente [nota 13]','','10079'),(81,'A Expedição Kon-Tiki','','10080'),(82,'O Bom Soldado Švejk','','10081'),(83,'Onde Vivem os Monstros [nota 14]','','10082'),(84,'O Poder do Pensamento Positivo','','10083'),(85,'A Cabana','','10084'),(86,'O Segredo','','10085'),(87,'Fear of Flying','','10086'),(88,'Duna','','10087'),(89,'A Culpa É das Estrelas','','10088'),(90,'Boa Noite Lua','','10089'),(91,'A História Sem Fim [nota 15]','','10090'),(92,'Adivinha Quanto Eu Te Amo','','10091'),(93,'Xógum - A Gloriosa Saga do Japão','','10092'),(94,'The Poky Little Puppy','','10093'),(95,'Os Pilares da Terra','','10094'),(96,'Como Fazer Amigos e Influenciar Pessoas','','10095'),(97,'O Perfume','','10096'),(98,'As Vinhas da Ira','','10097'),(99,'O Encantador de Cavalos','','10098'),(100,'A Sombra do Vento','','10099'),(101,'Totto-chan  the Little Girl at the Window','','10100'),(102,'O Guia do Mochileiro das Galáxias','','10101'),(103,'As Terças com Morrie','','10102'),(104,'O Pequeno Rincão de Deus','','10103'),(105,'Va\' dove ti porta il cuore','','10104'),(106,'Uma Dobra no Tempo','','10105'),(107,'O Velho e o Mar','','10106'),(108,'The Outsiders','','10107'),(109,'A Fantástica Fábrica de Chocolate [nota 16]','','10108'),(110,'Vida depois da Vida','','10109'),(111,'Norwegian Wood','','10110'),(112,'Peyton Place','','10111'),(113,'A Peste','','10112'),(114,'Humanidade Perdida [nota 17]','','10113'),(115,'O Macaco Nu','','10114'),(116,'Em Busca de Sentido','','10115'),(117,'Divina Comédia','','10116'),(118,'O Mundo Se Despedaça [nota 18]','','10117'),(119,'O Profeta','','10118'),(120,'O Exorcista','','10119'),(121,'O Grufalo','','10120'),(122,'Ardil 22 [nota 19]','','10121'),(123,'O Buraco da Agulha','','10122'),(124,'Uma Breve História do Tempo','','10123'),(125,'O Gato com Chapéu','','10124'),(126,'Uma Vida Interrompida [nota 20]','','10125'),(127,'(Cisnes Selvagens)','','10126'),(128,'Santa Evita','','10127'),(129,'A Noite','','10128'),(130,'O Caçador de Pipas [nota 21]','','10129'),(131,'Confucius from the Heart','','10130'),(132,'A Mulher Total','','10131'),(133,'Knowledge-value Revolution','','10132'),(134,'Problems in China\'s Socialist Economy','','10133'),(135,'What Color is Your Parachute?','','10134'),(136,'Dieta Dukan','','10135'),(137,'Os Prazeres do Sexo','','10136'),(138,'The Gospel According to Peanuts','','10137'),(139,'A Vida de Pi','','10138'),(140,'O Doador','','10139');
/*!40000 ALTER TABLE `livros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-29 18:13:14
