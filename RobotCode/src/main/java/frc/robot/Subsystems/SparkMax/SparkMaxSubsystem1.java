package frc.robot.Subsystems.SparkMax;

import edu.wpi.first.wpilibj2.command.SubsystemBase;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.networktables.NetworkTableEntry;

import com.revrobotics.CANSparkMax;
public class SparkMaxSubsystem1 extends SubsystemBase{

  private CANSparkMax sparkMax1;
  private NetworkTableInstance ntInstance = NetworkTableInstance.getDefault();
  private NetworkTable ntTable = ntInstance.getTable("SparkMaxSubsystem1");
  private NetworkTableEntry ntEntry = ntTable.getEntry("SparkMax1");

  public SparkMaxSubsystem1() {
    sparkMax1 = new CANSparkMax(1, com.revrobotics.CANSparkMaxLowLevel.MotorType.kBrushless);
  }
  
}
