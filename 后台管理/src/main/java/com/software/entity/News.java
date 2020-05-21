package com.software.entity;

import com.sun.javafx.beans.IDProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;
import lombok.experimental.Accessors;
import org.springframework.format.annotation.DateTimeFormat;

import javax.xml.bind.annotation.XmlID;

@Data
@AllArgsConstructor
@NoArgsConstructor
@ToString
@Accessors(chain = true)
public class News {

    //nid    |    title    | content  |    nimg     |    ntime    |  publisher  |mname|evaluation|source|
    int nid;
    String title;
    String content;
    String nimg;

    @DateTimeFormat
    String ntime;
    String publisher;
    String mname;
    String evaluation;
    String source;
}
