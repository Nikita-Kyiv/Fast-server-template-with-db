from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status, Response, Cookie
from typing import Optional
from sqlalchemy.ext.asyncio import async_sessionmaker
import os
import uuid

from app.db.database import db
from app.db.CRUD.Example import ExampleCRUD
router = APIRouter()


@router.post("/example")
async def create_example(
    example_field: str = Form(...),
    session: Optional[async_sessionmaker] = Depends(db.create_as_session_maker),
):
    example_data = {"example_field": example_field}
    created_example = await ExampleCRUD.create_example(session, example_data)
    return created_example