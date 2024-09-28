package frc.robot.Subsystems;

public enum MotorType {
  NONE(0),
  TALONFX(1),
  SPARKMAX(2),
  SPARKFLEX(3);

  private int type;

  MotorType(int type) {
    this.type= type;
  }

  public int getType(){
    return type;
  }

  public void setType(int type){
    this.type = type;
  }
}
