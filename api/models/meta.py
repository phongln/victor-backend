from api.models import BaseModel, BaseSchema, apply_schema


@apply_schema('RefContactSchema')
class RefContact(BaseModel):
    __tablename__ = 'ref_contact'


class RefContactSchema(BaseSchema):
    class Meta:
        model = RefContact
        fields = ['contact_type_id', 'contact_type']


@apply_schema('RefMediaSchema')
class RefMedia(BaseModel):
    __tablename__ = 'ref_meta'


class RefMediaSchema(BaseSchema):
    class Meta:
        model = RefMedia
        fields = ['media_id', 'media_name']


@apply_schema('RefSkillSchema')
class RefSkill(BaseModel):
    __tablename__ = 'ref_skill'


class RefSkillSchema(BaseSchema):
    class Meta:
        model = RefSkill
        fields = ['skill_id', 'skill_name']


@apply_schema('RefTopicSchema')
class RefTopic(BaseModel):
    __tablename__ = 'ref_topic'


class RefTopicSchema(BaseSchema):
    class Meta:
        model = RefTopic
        fields = ['topic_id', 'topic_name', 'description']
