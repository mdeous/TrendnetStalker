# -*- coding: utf-8 -*-

from TrendnetStalker import settings

from peewee import SqliteDatabase, Model, RawQuery
from peewee import CharField, FloatField, BooleanField, ForeignKeyField


class TrendnetStalkerDB(SqliteDatabase):
    def connect(self):
        super(TrendnetStalkerDB, self).connect()
        pragma = RawQuery(BaseModel, "PRAGMA foreign_keys = ON;")
        self.execute(pragma)


class BaseModel(Model):
    class Meta:
        database = TrendnetStalkerDB(settings.DATABASE)


class Camera(BaseModel):
    url = CharField(max_length=44, unique=True)
    lat = FloatField()
    lng = FloatField()
    is_dead = BooleanField(default=False)

    def __str__(self):
        return "<Camera url=%r lat=%r lng=%r>" % (self.url, self.lat, self.lng)


class Comment(BaseModel):
    content = CharField(max_length=1024)
    camera = ForeignKeyField(Camera, related_name='comments')

    def __str__(self):
        content = self.content[:10] + '[...]' if len(self.content) > 10 else self.content
        return "<Comment %r>" % content


class Tag(BaseModel):
    name = CharField(max_length=20)

    def __str__(self):
        return "<Tag %r>" % self.name


class CameraTag(BaseModel):
    camera = ForeignKeyField(Camera)
    tag = ForeignKeyField(Tag)

    def __str__(self):
        return "<CameraTag camera=%r tag=%r>" % (self.camera.url, self.tag.name)
