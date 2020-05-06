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
public class Ction {
    private int mid;
    private String cname;
    private String cimg;
    private String years;
    private String explain;
    private String size;
    private String src;
}
