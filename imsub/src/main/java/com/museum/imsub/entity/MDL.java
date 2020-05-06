package com.museum.imsub.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;
import lombok.experimental.Accessors;

@Data
@AllArgsConstructor
@NoArgsConstructor
@ToString
@Accessors(chain = true)
public class MDL {
    private int mid;
    private String mname;
    private String mimg;
    private String evaluat;
    private String grade;
    private String basic_info;
    private String other_info;
    private Double grade_1;
    private Double grade_2;
    private Double grade_3;

}
