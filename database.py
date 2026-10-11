
# 개인 로컬 DB 연결 테스트용
# 공용 Git 업로드 아직 안할거임 (비밀번호 포함)
from fastapi import APIRouter, Depends, Request
from sqlmodel import Session, create_engine,text


def get_session():
    with Session(engine) as session:
        yield session
        session.commit()


DATABASE_URL = 'mysql+pymysql://root:human123$@127.0.0.1:3306/human'

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# 연결 확인 잘 되었는지 확인용
if __name__ == "__main__":
    with engine.connect() as conn:
        result = conn.execute(text("SELECT DATABASE()"))
        print("연결 성공:", result.scalar())


