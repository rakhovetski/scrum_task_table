from sqlalchemy import select, insert, update, delete

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def find_by_id(cls, id):
        async with async_session_maker() as session:
            query = select(cls.model).where(
                cls.model.id == id
            )
            
            result = await session.execute(query)
            return result.scalars().one_or_none()
        
        
    @classmethod
    async def insert(cls, **kwargs):
        async with async_session_maker() as session:
            query = insert(cls.model).values(
                **kwargs
            ).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return {'id': result.fetchone()[0],
                    **kwargs}
        
    
    @classmethod
    async def update(cls, id, **kwargs):
        async with async_session_maker() as session:
            query = update(cls.model).where(
                cls.model.id == id
            ).values(
                **kwargs
            ).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return {'id': result.fetchone()[0],
                    **kwargs}
        
        
    @classmethod
    async def delete(cls, id):
        async with async_session_maker() as session:
            query = delete(cls.model).where(
                cls.model.id == id
            ).returning(cls.model.id)
            await session.execute(query)
            await session.commit()
            return {'id': id}