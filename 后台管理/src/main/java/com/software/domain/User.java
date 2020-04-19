package com.software.domain;
public class User {
	private String uid;
	private String upwd;
	private String uname;
	private boolean gender;
	private String authority;
	private String introduction;
	private String icon;
	
	public User() {
		// TODO Auto-generated constructor stub
	}

	public User(String uid, String upwd, String uname, boolean gender, String authority, String introduction,
			String icon) {
		super();
		this.uid = uid;
		this.upwd = upwd;
		this.uname = uname;
		this.gender = gender;
		this.authority = authority;
		this.introduction = introduction;
		this.icon = icon;
	}

	@Override
	public String toString() {
		return "User [uid=" + uid + ", upwd=" + upwd + ", uname=" + uname + ", gender=" + gender + ", authority="
				+ authority + ", introduction=" + introduction + ", icon=" + icon + "]";
	}

	public String getUid() {
		return uid;
	}

	public void setUid(String uid) {
		this.uid = uid;
	}

	public String getUpwd() {
		return upwd;
	}

	public void setUpwd(String upwd) {
		this.upwd = upwd;
	}

	public String getUname() {
		return uname;
	}

	public void setUname(String uname) {
		this.uname = uname;
	}

	public boolean isGender() {
		return gender;
	}

	public void setGender(boolean gender) {
		this.gender = gender;
	}

	public String getAuthority() {
		return authority;
	}

	public void setAuthority(String authority) {
		this.authority = authority;
	}

	public String getIntroduction() {
		return introduction;
	}

	public void setIntroduction(String introduction) {
		this.introduction = introduction;
	}

	public String getIcon() {
		return icon;
	}

	public void setIcon(String icon) {
		this.icon = icon;
	}
	
	
}
