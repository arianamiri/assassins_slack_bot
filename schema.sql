-- Main User Table
CREATE TABLE `agents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_name` varchar(50) NOT NULL,
  `code_name` varchar(50) DEFAULT NULL,
  `slack_handle` varchar(50) DEFAULT NULL,
  `is_moderator` tinyint(4) DEFAULT '0',
  `is_alive` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code_name` (`code_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- Contract Table
CREATE TABLE `contracts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) NOT NULL,
  `target_id` int(11) NOT NULL,
  `bounty` int(11) NOT NULL,
  `is_open` tinyint(4) NOT NULL DEFAULT '1',
  `is_successful` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `owner_target_unique` (`owner_id`,`target_id`),
  KEY `target_id` (`target_id`),
  CONSTRAINT `contracts_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `agents` (`id`),
  CONSTRAINT `contracts_ibfk_2` FOREIGN KEY (`target_id`) REFERENCES `agents` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
