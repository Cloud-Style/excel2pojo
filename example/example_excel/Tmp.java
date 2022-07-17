package com.test;

import lombok.Data;
import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;
    
/**
 * @author 尺规kit
 * @date 2022-07-17
 */
@Data
public class Tmp {
    
    /**
     * 数据id
     */
    @JsonAlias({"data_id", "dataId"})
    @JsonProperty("data_id")
    private String dataId;
    
    /**
     * 操作类型
新增
删除

     */
    @JsonAlias({"operation_type", "operationType"})
    @JsonProperty("operation_type")
    private String operationType;
    
    /**
     * 被操作数据信息
     */
    @JsonAlias("original")
    @JsonProperty("original")
    private Object original;
    
    /**
     * 被操作数据id
     */
    @JsonAlias("id")
    @JsonProperty("id")
    private String id;
    
    /**
     * 数据的类型
     */
    @JsonAlias("type")
    @JsonProperty("type")
    private String type;
    
    /**
     * 名字
     */
    @JsonAlias("name")
    @JsonProperty("name")
    private String name;
    
    /**
     * 编号
     */
    @JsonAlias("number")
    @JsonProperty("number")
    private String number;
    
    /**
     * 数据推送时间
     */
    @JsonAlias({"publish_date", "publishDate"})
    @JsonProperty("publish_date")
    @JsonFormat(pattern = "yyyy-MM-dd", timezone = "GMT+8")
    private Date publishDate;
    
    /**
     * 年龄
     */
    @JsonAlias("age")
    @JsonProperty("age")
    private Integer age;
    
    /**
     * 有相关关系的朋友
     */
    @JsonAlias("friends")
    @JsonProperty("friends")
    private List friends;
    
    /**
     * 朋友的名字
     */
    @JsonAlias("name")
    @JsonProperty("name")
    private String name;
    
    /**
     * 朋友的年龄
     */
    @JsonAlias("age")
    @JsonProperty("age")
    private Integer age;
        
}
    