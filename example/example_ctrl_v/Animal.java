package com.test.animal;

import lombok.Data;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonAlias;
    
/**
 * @author 尺规kit
 * @date 2022-07-17
 */
@Data
public class Animal {
    
    /**
     * 名字
     */
    @JsonAlias("name")
    private String name;
    
    /**
     * 编号
     */
    @JsonAlias("number")
    private String number;
    
    /**
     * 数据推送时间
     */
    @JsonAlias({"publish_date", "publishDate"})
    @JsonFormat(pattern = "yyyy-MM-dd", timezone = "GMT+8")
    private Date publishDate;
    
    /**
     * 年龄
     */
    @JsonAlias("age")
    private Integer age;
    
    /**
     * 有相关关系的朋友
     */
    @JsonAlias("friends")
    private List friends;
    
    /**
     * 朋友的名字
     */
    @JsonAlias("name")
    private String name;
    
    /**
     * 朋友的年龄
     */
    @JsonAlias("age")
    private Integer age;
        
}
    