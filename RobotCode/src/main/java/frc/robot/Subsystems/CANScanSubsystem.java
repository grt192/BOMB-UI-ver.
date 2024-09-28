package frc.robot.Subsystems;

import com.ctre.phoenix6.hardware.TalonFX;
import com.revrobotics.CANSparkMax;
import com.revrobotics.CANSparkFlex;
import com.revrobotics.CANSparkLowLevel;

import frc.robot.Subsystems.MotorType;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class CANScanSubsystem extends SubsystemBase{

  private TalonFX testCTREController;
  private CANSparkMax testSparkMaxController;
  private CANSparkFlex testSparkFlexController;
  
  private NetworkTableInstance nTableInstance;
  private NetworkTable ntTable;
  private NetworkTableEntry ntEntry;

  private long motors[] = new long[21];
  /*
  -1 for no motor
  1 for TalonFX
  2 for SparkMax
  3 for SparkFlex
  */  

  public CANScanSubsystem() {
    for(int id = 0; id < 21; id++){
      motors[id] = -1;
    }

    nTableInstance = NetworkTableInstance.getDefault();
    ntTable = nTableInstance.getTable("Publish");
    ntEntry = ntTable.getEntry("Motors");

  }

  @Override
  public void periodic() {
    for(int id = 0; id < 21; id++){
      try{
        testCTREController = new TalonFX(id);
        if(testCTREController.isAlive())
          motors[id] = 1;
      }
      catch(Exception e){
      }

      try{
        testSparkMaxController = new CANSparkMax(
          id, CANSparkLowLevel.MotorType.kBrushless);
        motors[id] = 2; 
      }
      catch(Exception e){
      }

      try{
        testSparkFlexController = new CANSparkFlex(
          id, CANSparkLowLevel.MotorType.kBrushless);
        motors[id] = 3;
      }
      catch(Exception e){
      }
    }
    ntEntry.setIntegerArray(motors);
    System.out.println("finished");
  }
}
