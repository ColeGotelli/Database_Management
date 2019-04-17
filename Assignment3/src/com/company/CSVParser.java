package com.company;

import java.sql.*;
import java.io.*;
import java.util.List;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;


public class CSVParser {

    private String mFileName;
    private Connection con;

    public CSVParser() {
        mFileName = null;
        con = null;
    }

    public CSVParser(String filename, Connection connection) {
        mFileName = filename;
        con = connection;
    }

    public String getmFileName() {
        return mFileName;
    }

    public void initDatabase() throws SQLException{
        clearDatabase();

        //Creates FirstName Table
        PreparedStatement s = con.prepareStatement(
                "CREATE IF NOT EXISTS FirstName(" +
                        "ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT," + //ID
                        "FName VARCHAR(20))" //FirstName

        );
        s.executeUpdate();

        //Creates LastName Table
        s = con.prepareStatement(
                "CREATE TABLE IF NOT EXISTS LastName(" +
                        "ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT," + //ID
                        "LName VARCHAR(20))" //LastName

        );
        s.executeUpdate();

        //Creates Age Table
        s = con.prepareStatement(
                "CREATE TABLE IF NOT EXISTS Age(" +
                        "ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT," + //ID
                        "Age INTEGER)" //Age

        );
        s.executeUpdate();

        //Creates Person Table
        s = con.prepareStatement(
                "CREATE TABLE IF NOT EXISTS Person(" +
                        "ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT," + //ID
                        "FirstName VARCHAR(20)," + //FirstName
                        "LastName VARCHAR(20)," + //LastName
                        "Age INTEGER)" //Age

        );
        s.executeUpdate();

        //Creates State Table
        s = con.prepareStatement(
                "CREATE TABLE IF NOT EXISTS State(" +
                        "ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT," + //ID
                        "State VARCHAR(20))" //State

        );
        s.executeUpdate();

        //Creates Location Table
        s = con.prepareStatement(
                "CREATE TABLE IF NOT EXISTS Location(" +
                        "ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT," + //ID
                        "City VARCHAR(50)," + //City
                        "State VARCHAR(20)," + //State
                        "Zip INTEGER)" //Zip

        );
        s.executeUpdate();
    }


    public static List<List<String>> readFile(String filename) throws FileNotFoundException {
        Scanner s = new Scanner(new File(filename));
        s.useDelimiter(",");

        List<List<String>> col = new ArrayList<List<String>>();

        while(s.hasNext()) { //Looks at each row and separates info relative to a ',' then inserts the row into list
            String temp = s.nextLine();
            List<String> row = Arrays.asList(temp.split(","));
            col.add(row);
        }
        s.close();

        return col;
    }


    public void parseCSV() {
        try {

            List<List<String>> records = readFile(getmFileName());

            for (List<String> record : records.subList(1, records.size())) {
                String firstName = record.get(0);
                String lastName = record.get(1);
                String age = record.get(2);
                String city = record.get(3);
                String state = record.get(4);
                String zip = record.get(5);


                int parameterindex = 1;
                int columnindex = 1;


                //Each prepared statement is used to insert into a table
                //First Name Table
                String sql1 = "INSERT INTO FirstName(FName) VALUES (?)";
                PreparedStatement stmt = con.prepareStatement( sql1, Statement.RETURN_GENERATED_KEYS);


                stmt.setString(1, firstName);
                stmt.executeUpdate();
                stmt.clearParameters();


                //Last Name Table
                String sql2 = "INSERT INTO LastName(lname) VALUES (?)";
                PreparedStatement stmt2 = con.prepareStatement(sql2, Statement.RETURN_GENERATED_KEYS);

                stmt2.setString(1, lastName);
                stmt2.executeUpdate();
                stmt2.clearParameters();


                //Age Table
                String sql3 = "INSERT INTO Age(age) VALUES (?)";
                PreparedStatement stmt3 = con.prepareStatement(sql3, Statement.RETURN_GENERATED_KEYS);

                stmt3.setString(1, age);
                stmt3.executeUpdate();
                stmt3.clearParameters();

                //Person Table
                String sql4 = "INSERT INTO Person(FirstName, LastName, Age) VALUES (?,?,?)";
                PreparedStatement stmt4 = con.prepareStatement(sql4);

                stmt4.setString(1, firstName);
                stmt4.setString(2, lastName);
                stmt4.setString(3, age);
                stmt4.executeUpdate();

                //State Table
                String sql5 = "INSERT INTO State(State) VALUES (?)";
                PreparedStatement stmt5 = con.prepareStatement(sql5);

                stmt5.setString(1, state);
                stmt5.executeUpdate();

                //Location Table
                String sql6 = "INSERT INTO Location(City, State, Zip) VALUES (?,?,?)";
                PreparedStatement stmt6 = con.prepareStatement(sql6);

                stmt6.setString(1, city);
                stmt6.setString(2, state);
                stmt6.setString(3, zip);
                stmt6.executeUpdate();

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void clearDatabase() throws SQLException {

        PreparedStatement s = con.prepareStatement("DROP TABLE IF EXISTS FirstName");
        s.executeUpdate();

        s = con.prepareStatement("DROP TABLE IF EXISTS LastName");
        s.executeUpdate();

        s = con.prepareStatement("DROP TABLE IF EXISTS Age");
        s.executeUpdate();

        s = con.prepareStatement("DROP TABLE IF EXISTS Person");
        s.executeUpdate();

        s = con.prepareStatement("DROP TABLE IF EXISTS State");
        s.executeUpdate();

        s = con.prepareStatement("DROP TABLE IF EXISTS Location");
        s.executeUpdate();

        s.close();
    }
}
