from pydantic import BaseModel, ConfigDict


class CreateLaunchConfigSchema(BaseModel):
    
    v0: float 
    angle_deg: float
    gravity: float

class LaunchConfigResponse(CreateLaunchConfigSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int