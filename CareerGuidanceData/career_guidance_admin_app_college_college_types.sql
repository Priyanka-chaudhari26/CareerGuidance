-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: career_guidance
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `admin_app_college_college_types`
--

DROP TABLE IF EXISTS `admin_app_college_college_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_app_college_college_types` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `college_id` bigint NOT NULL,
  `collegetype_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_app_college_colleg_college_id_collegetype_i_81f09044_uniq` (`college_id`,`collegetype_id`),
  KEY `admin_app_college_co_collegetype_id_1de986bd_fk_admin_app` (`collegetype_id`),
  CONSTRAINT `admin_app_college_co_college_id_447bf87a_fk_admin_app` FOREIGN KEY (`college_id`) REFERENCES `admin_app_college` (`id`),
  CONSTRAINT `admin_app_college_co_collegetype_id_1de986bd_fk_admin_app` FOREIGN KEY (`collegetype_id`) REFERENCES `admin_app_collegetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_app_college_college_types`
--

LOCK TABLES `admin_app_college_college_types` WRITE;
/*!40000 ALTER TABLE `admin_app_college_college_types` DISABLE KEYS */;
INSERT INTO `admin_app_college_college_types` VALUES (16,6,1),(18,6,2),(17,6,10),(19,7,5),(20,8,2),(23,9,2),(24,9,6),(22,9,8),(21,9,16);
/*!40000 ALTER TABLE `admin_app_college_college_types` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-29 22:14:29
