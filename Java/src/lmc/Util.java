package lmc;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class Util
{
    static String readFile(String filename)
    {
        File f = new File(filename);
        try {
            byte[] bytes = Files.readAllBytes(f.toPath());
            return new String(bytes,"UTF-8");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "";
    }
}
