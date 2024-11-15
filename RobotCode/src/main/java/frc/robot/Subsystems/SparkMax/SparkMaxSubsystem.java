package frc.robot.Subsystems.SparkMax;

import frc.robot.Constants;

import java.util.EnumSet;

import com.ctre.phoenix6.hardware.TalonFX;
import com.revrobotics.CANSparkMax;
import com.revrobotics.CANSparkFlex;
import com.revrobotics.CANSparkLowLevel;

import frc.robot.Subsystems.MotorType;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableEvent;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class SparkMaxSubsystem extends SubsystemBase{

    private int motorID;
    private CANSparkMax motor;

    private NetworkTableInstance nTableInstance;
    private NetworkTable ntTable;
    private String ntSpeedEntryName;
    private NetworkTableEntry 
        ntSpeedEntry, ntTempEntry, ntCurrentEntry, ntVoltageEntry;


    public SparkMaxSubsystem(int motorID) {
        this.motorID = motorID;
        motor = new CANSparkMax(motorID, CANSparkLowLevel.MotorType.kBrushless);

        nTableInstance = NetworkTableInstance.getDefault();
        ntTable = nTableInstance.getTable(Constants.ROOT_TABLE_NAME);
        ntSpeedEntryName = this.motorID + "Speed";
        ntSpeedEntry = ntTable.getEntry(ntSpeedEntryName);
        ntTempEntry = ntTable.getEntry(motorID + "Temp");
        ntCurrentEntry = ntTable.getEntry(motorID + "Current");
        ntVoltageEntry = ntTable.getEntry(motorID + "Voltage");


        ntTable.addListener(
            ntSpeedEntryName,
            EnumSet.of(NetworkTableEvent.Kind.kValueAll),
            (table, key, event) -> {
                // double speed = ntSpeedEntry.getDouble(0);
                double speed = event.valueData.value.getDouble();
                motor.set(speed/100 );
                System.out.print(this.motorID + "Speed: " + speed);
            }
        );

    }

    @Override
    public void periodic() {
        double FPGATime = Timer.getFPGATimestamp();
        // ntSpeedEntry.setDouble(FPGATime);
        ntCurrentEntry.setDouble(FPGATime);
        ntVoltageEntry.setDouble(FPGATime);
        ntTempEntry.setDouble(FPGATime);
    }
}
