package com.company;
import java.sql.*;

public class Main {

    public static void main(String[] args) throws SQLException{

        Connection con = null;

        try {
            con = DBConfig.getMySqlConnection("35.203.155.186", "assignment3", "cole");

            System.out.println("CONNECTION TO SQL SERVER SUCCESSFUL");

            if (con.isClosed()) {
                con = DBConfig.getMySqlConnection("35.203.155.186", "assignment3", "cole");
            }


            String fileName = "./testCSV.csv";
            CSVParser csv = new CSVParser(fileName, con);
            csv.readFile(fileName);
            csv.initDatabase();
            csv.parseCSV();

        }
        catch (Exception e) {
            e.printStackTrace();
        }
        finally {
            con.close();
        }
    }
}
