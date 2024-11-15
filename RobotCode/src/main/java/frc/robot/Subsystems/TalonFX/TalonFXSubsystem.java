package frc.robot.Subsystems.TalonFX;

import java.util.EnumSet;

import com.ctre.phoenix6.hardware.TalonFX;

import edu.wpi.first.wpilibj2.command.SubsystemBase;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableEvent;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;

public class TalonFXSubsystem extends SubsystemBase{
    private int motorID;
    private TalonFX motor;

    private NetworkTableInstance nTableInstance;
    private NetworkTable ntTable;
    private String ntSpeedEntryName;
    private NetworkTableEntry ntSpeedEntry;

    public TalonFXSubsystem(int motorID) {
        this.motorID = motorID;
        motor = new TalonFX(motorID);

        nTableInstance = NetworkTableInstance.getDefault();
        ntTable = nTableInstance.getTable("TalonFX");
        ntSpeedEntryName = this.motorID + "Speed";
        ntSpeedEntry = ntTable.getEntry(ntSpeedEntryName);

        ntTable.addListener(
            ntSpeedEntryName,
            EnumSet.of(NetworkTableEvent.Kind.kValueAll),
            (table, key, event) -> {
                double speed = ntSpeedEntry.getDouble(0);
                System.out.print(this.motorID + "Speed: " + speed);
                motor.set(speed);
            }
        );
    } 
}
