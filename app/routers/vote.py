from fastapi import FastAPI, Response, status, Depends, HTTPException, APIRouter
from typing import List, Optional
from .. import models, oauth2
from ..schema import Vote
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote:Vote, db:Session=Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    
    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added a vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully removed a vote"}
        
        
    