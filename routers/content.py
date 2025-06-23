from fastapi import APIRouter

router = APIRouter(prefix="/content", tags=["Content"])

@router.get("/lectures")
def get_lectures():
    return {"lectures": ["Lecture 1", "Lecture 2"]}

@router.get("/notes")
def get_notes():
    return {"notes": ["Note 1", "Note 2"]}

@router.get("/dpps")
def get_dpps():
    return {"dpps": ["DPP 1", "DPP 2"]}

@router.get("/tests")
def get_tests():
    return {"tests": ["Test 1", "Test 2"]}
