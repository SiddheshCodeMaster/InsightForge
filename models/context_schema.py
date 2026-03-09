from pydantic import BaseModel
from typing import Dict, List, Any, Optional
import pandas as pd


class AnalysisContext(BaseModel):
    dataset_path: str
    dataset_profile: Optional[Dict[str, Any]] = None
    column_intelligence: Optional[Dict[str, Any]] = None
    revenue_trends: Optional[Dict[str, float]] = None
    hypotheses: Optional[List[str]] = None
    evidence: Optional[Dict[str, Any]] = None
    insights: Optional[List[str]] = None
    dataframe: Optional[Any] = None

    class Config:
        arbitrary_types_allowed = True
