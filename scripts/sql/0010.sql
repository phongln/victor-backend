CREATE TABLE user_profile (
 user_id BIGSERIAL NOT NULL,
 status SMALLINT/* -1 - deleted, 0 - inactive, 1 - active, 2 - verifying */,
 username VARCHAR(128) NOT NULL,
 password VARCHAR(64) NOT NULL,
 fullname VARCHAR(128),
 nickname VARCHAR(128),
 birthday DATE,
 gender CHAR(1),
 createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
 updatedOn DATE DEFAULT CURRENT_DATE
);


ALTER TABLE user_profile ADD CONSTRAINT user_profile_pkey PRIMARY KEY (user_id);
COMMENT ON COLUMN "user_profile"."status" IS '-1 - deleted, 0 - inactive, 1 - active, 2 - verifying';


CREATE TABLE ref_media (
 media_id BIGSERIAL NOT NULL,
 media_name VARCHAR(64) NOT NULL,
 ord_num SMALLINT
);


ALTER TABLE ref_media ADD CONSTRAINT ref_media_pkey PRIMARY KEY (media_id);

CREATE TABLE user_media (
 id BIGSERIAL NOT NULL,
 user_id INTEGER NOT NULL,
 media_id SMALLINT,
 url VARCHAR(1024)
);


ALTER TABLE user_media ADD CONSTRAINT user_media_pkey PRIMARY KEY (id);
ALTER TABLE user_media ADD CONSTRAINT user_media_combo1 UNIQUE (user_id, media_id);

CREATE TABLE user_info (
 user_id INTEGER NOT NULL,
 brief_description TEXT,
 education VARCHAR(128),
 position VARCHAR(128),
 company_name VARCHAR(128)
);


ALTER TABLE user_info ADD CONSTRAINT user_info_pkey PRIMARY KEY (user_id);

CREATE TABLE post (
 post_id BIGSERIAL NOT NULL,
 user_id INTEGER NOT NULL,
 status SMALLINT NOT NULL/* -1 -deleted, 0 - inactive, 1 - active, 2 - not publish */,
 title VARCHAR(512),
 content TEXT,
 createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
 updatedAt TIMESTAMP
);


ALTER TABLE post ADD CONSTRAINT post_pkey PRIMARY KEY (post_id);
COMMENT ON COLUMN "post"."status" IS '-1 -deleted, 0 - inactive, 1 - active, 2 - not publish';

CREATE TABLE ref_topic (
 topic_id BIGSERIAL NOT NULL,
 topic_name VARCHAR(64) NOT NULL,
 description TEXT NOT NULL,
 ord_num SMALLINT
);


ALTER TABLE ref_topic ADD CONSTRAINT ref_topic_pkey PRIMARY KEY (topic_id);

CREATE TABLE post_topic (
 id BIGSERIAL NOT NULL,
 post_id BIGINT NOT NULL,
 topic_id INTEGER NOT NULL,
 user_id INTEGER NOT NULL
);


ALTER TABLE post_topic ADD CONSTRAINT post_topic_pkey PRIMARY KEY (id);
ALTER TABLE post_topic ADD CONSTRAINT post_topic_combo1 UNIQUE (topic_id, post_id);

CREATE TABLE ref_skill (
 skill_id BIGSERIAL NOT NULL,
 skill_name VARCHAR(128) NOT NULL,
 ord_num INTEGER
);


ALTER TABLE ref_skill ADD CONSTRAINT ref_skill_pkey PRIMARY KEY (skill_id);

CREATE TABLE user_skill (
 id BIGSERIAL NOT NULL,
 user_id INTEGER NOT NULL,
 skill_id INTEGER NOT NULL
);


ALTER TABLE user_skill ADD CONSTRAINT user_skill_pkey PRIMARY KEY (id);
ALTER TABLE user_skill ADD CONSTRAINT user_skill_combo1 UNIQUE (user_id, skill_id);

CREATE TABLE user_experience (
 id BIGSERIAL NOT NULL,
 user_id INTEGER NOT NULL,
 description INTEGER,
 updatedAt TIMESTAMP,
 company_name VARCHAR(128),
 startedOn DATE,
 endedOn DATE,
 is_current CHAR(1)
);


ALTER TABLE user_experience ADD CONSTRAINT user_experience_pkey PRIMARY KEY (id);

CREATE TABLE ref_contact (
 contact_type_id BIGSERIAL NOT NULL,
 contact_type VARCHAR(64) NOT NULL,
 ord_num SMALLINT
);


ALTER TABLE ref_contact ADD CONSTRAINT ref_contact_pkey PRIMARY KEY (contact_type_id);


ALTER TABLE user_media ADD CONSTRAINT user_media_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE user_media ADD CONSTRAINT user_media_media_id_fkey FOREIGN KEY (media_id) REFERENCES ref_media(media_id);
ALTER TABLE user_info ADD CONSTRAINT user_info_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE post ADD CONSTRAINT post_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE post_topic ADD CONSTRAINT post_topic_post_id_fkey FOREIGN KEY (post_id) REFERENCES post(post_id);
ALTER TABLE post_topic ADD CONSTRAINT post_topic_topic_id_fkey FOREIGN KEY (topic_id) REFERENCES ref_topic(topic_id);
ALTER TABLE post_topic ADD CONSTRAINT post_topic_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE user_skill ADD CONSTRAINT user_skill_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE user_skill ADD CONSTRAINT user_skill_skill_id_fkey FOREIGN KEY (skill_id) REFERENCES ref_skill(skill_id);
ALTER TABLE user_experience ADD CONSTRAINT user_experience_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_profile(user_id);