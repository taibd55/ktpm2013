

import static org.junit.Assert.*;

import org.junit.Test;

public class GiaiPTB1Test {
	
	GiaiPTB1 myTest = new GiaiPTB1();
	
	@Test
	public void test1(){
		assertEquals("must be -1", -1, myTest.handle(1,1));
	}
	
	@Test
	public void test2(){
		assertEquals("must be 9", 9, myTest.handle(10,-90));
	}

}
