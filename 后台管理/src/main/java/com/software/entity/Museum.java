package com.software.entity;

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
public class Museum {
    int mid;
    String mname;
    String ming;
    String evaluate;
    double grade;
    double grade_1;
    double grade_2;
    double grade_3;
    String basic_info;
    String other_info;
}
