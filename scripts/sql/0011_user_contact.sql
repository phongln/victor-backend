CREATE TABLE user_contact (
 id BIGSERIAL NOT NULL,
 user_id INTEGER NOT NULL,
 contact_type_id SMALLINT NOT NULL,
 contact_name VARCHAR(512),
 ord_num SMALLINT NOT NULL DEFAULT 1
);


CREATE INDEX user_contact_combo on user_contact(user_id, contact_type_id);
ALTER TABLE user_contact ADD CONSTRAINT user_contact_pkey PRIMARY KEY (id);

ALTER TABLE user_contact ADD CONSTRAINT user_contact_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE user_contact ADD CONSTRAINT user_contact_contact_type_id_fkey FOREIGN KEY (contact_type_id) REFERENCES ref_contact(contact_type_id);
