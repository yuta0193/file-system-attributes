from controls.database import db
from models import User
from datetime import datetime

def run():
    # 新しいユーザーを作成
    new_user = User(name="test", created_at=datetime.now(), updated_at=datetime.now())

    # データベースセッションに追加
    db.session.add(new_user)

    # 変更をコミット
    db.session.commit()
