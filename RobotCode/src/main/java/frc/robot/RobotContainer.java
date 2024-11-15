package frc.robot;

import frc.robot.Subsystems.SparkMax.SparkMaxSubsystem;
import frc.robot.Subsystems.TalonFX.TalonFXSubsystem;

public class RobotContainer {
    private SparkMaxSubsystem[] sparkMaxSubsystems = new SparkMaxSubsystem[5];
    private TalonFXSubsystem[] talonFXSubsystems = new TalonFXSubsystem[5];

    public RobotContainer() {
        for(int i = 1; i<= 2; i++){
            sparkMaxSubsystems[i] = new SparkMaxSubsystem(i);
        }
        for(int i = 3; i <= 4; i++){
            talonFXSubsystems[i] = new TalonFXSubsystem(i);
        }
    }
  
}
