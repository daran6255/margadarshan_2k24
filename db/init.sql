CREATE USER 'wvf_candidates_profile' @'localhost' IDENTIFIED BY 'wvf@sp123&';
CREATE DATABASE IF NOT EXISTS candidates_profile;

GRANT ALL PRIVILEGES ON candidates_profile.* TO 'wvf_candidates_profile' @'localhost';

FLUSH PRIVILEGES;

USE candidates_profile;

CREATE TABLE IF NOT EXISTS candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('male', 'female', 'other') NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    category ENUM('PWD', 'Non-PWD', 'EWS', 'Women', 'LGBTQ', 'Retired person') NOT NULL,
    disability_type VARCHAR(100) NOT NULL,
    disability_percentage INT(100),
    highest_qualification VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    graduation_year YEAR NOT NULL,
    domain ENUM('IT', 'BFSI', 'MS Office', 'Data Visualization') NOT NULL,
    typing_speed VARCHAR(15) NOT NULL,
    quality VARCHAR(15) NOT NULL,
    experience ENUM('0-1 years', '1-3 years', '3-5 years', '5+ years') NOT NULL,
    photo VARCHAR(255) NOT NULL,
    resume VARCHAR(255) NOT NULL,
    video VARCHAR(255) NOT NULL,
    pdf VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id INT,
    skill_name VARCHAR(255),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);